from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from management_api.models import Admin, Branch, Staff, Doctor, Patient
from management_api.serializers import AdminSerializer, BranchSerializer, StaffSerializer, DoctorSerializer, PatientSerializer, AuthenticateAdminSerializer, AuthenticateStaffSerializer, AuthenticateDoctorSerializer

# Create your views here.

#List of Registered Admin
@api_view(['GET'])
@csrf_exempt
def admin_list(request):
    if request.method == 'GET':
        allAdmins = Admin.objects.all()
        serializer = AdminSerializer(allAdmins, many=True)
        return Response(serializer.data)



#List of Registered Staff
@api_view(['GET'])
@csrf_exempt
def staff_list(request):
    if request.method == 'GET':
        allStaff = Staff.objects.all()
        serializer = StaffSerializer(allStaff, many=True)
        return Response(serializer.data)    



#List of Registered Branch
@api_view(['GET'])
@csrf_exempt
def branch_list(request):
    if request.method == 'GET':
        allBranches = Branch.objects.all()
        serializer = BranchSerializer(allBranches, many=True)
        return Response(serializer.data)



#List of Registered Patients
@api_view(['GET'])
@csrf_exempt
def patient_list(request):
    if request.method == 'GET':
        allPatients = Patient.objects.all()
        serializer = PatientSerializer(allPatients, many=True)
        return Response(serializer.data)



#List of Registered Doctors
@api_view(['GET'])
@csrf_exempt
def doctor_list(request):
    if request.method == 'GET':
        allDoctors = Doctor.objects.all()
        serializer = DoctorSerializer(allDoctors, many=True)
        return Response(serializer.data)



#Staff Login
@api_view(['POST'])
@csrf_exempt
def staff_login(request):
    if request.method =='POST':
        staff_authenticate_serializer=AuthenticateStaffSerializer(data=request.data)
        staff_authenticate_serializer.is_valid(raise_exception=True)          #Bad Request, 400 returned
    if(staff_authenticate_serializer.authenticate_staff_function()):
        return Response({'Authentication':True}, status=200)
    else:
        return Response({'Authentication':False}, status=401)
   


#Admin Login
@api_view(['POST'])
@csrf_exempt
def admin_login(request):
    if request.method =='POST':
        admin_authenticate_serializer=AuthenticateAdminSerializer(data=request.data)
        admin_authenticate_serializer.is_valid(raise_exception=True)          #Bad Request, 400 returned
    if(admin_authenticate_serializer.authenticate_admin_function()):
        return Response({'Authentication':True}, status=200)
    else:
        return Response({'Authentication':False}, status=401)



#Doctor Login
@api_view(['POST'])
@csrf_exempt
def doctor_login(request):
    if request.method =='POST':
        doctor_authenticate_serializer=AuthenticateDoctorSerializer(data=request.data)
        doctor_authenticate_serializer.is_valid(raise_exception=True)          #Bad Request, 400 returned
    if(doctor_authenticate_serializer.authenticate_doctor_function()):
        return Response({'Authentication':True}, status=200)
    else:
        return Response({'Authentication':False}, status=401)
	


# Create Branch
@api_view(['POST'])
@csrf_exempt
def create_branch(request):          #request.data is a dictionary
    if request.method =='POST':
        admin_authenticate_serializer=AuthenticateAdminSerializer(data=request.data['admin'])
        
        admin_authenticate_serializer.is_valid(raise_exception=True)          #Bad Request, 400 returned

        if(admin_authenticate_serializer.authenticate_admin_function()):
            
            branch_serializer=BranchSerializer(data=request.data['branch'])
            if(branch_serializer.is_valid(raise_exception=True)):             #Bad Request, 400 returned
                branch_serializer.save()
                print("Right Branch Information")
            else:
                print("Wrong Branch Information")                             #Bad Request (Handled above)

        else:
            return Response(admin_authenticate_serializer.errors,status=401)  #Unauthorized, 401 returned

        return Response(branch_serializer.validated_data,status=200)



# Create Staff
@api_view(['POST'])
@csrf_exempt
def create_staff(request):          #request.data is a dictionary
    if request.method =='POST':
        admin_authenticate_serializer=AuthenticateAdminSerializer(data=request.data['admin'])
        
        admin_authenticate_serializer.is_valid(raise_exception=True)          #Bad Request, 400 returned
        staff_serializer_for_branch=None
        if(admin_authenticate_serializer.authenticate_admin_function()):
            
            staff_serializer=StaffSerializer(data=request.data['staff'])
            if(staff_serializer.is_valid(raise_exception=True)):             #Bad Request, 400 returned
                # print(staff_serializer.save())
                print("Right Staff Information")
                staff_serializer_for_branch=StaffSerializer(staff_serializer.save()) #Serializing the object

            else:
                print("Wrong Staff Information")                             #Bad Request (Handled above)

        else:
            return Response(admin_authenticate_serializer.errors,status=401)  #Unauthorized, 401 returned

        return Response(staff_serializer_for_branch.data,status=200)


# Create Patient
@api_view(['POST'])
@csrf_exempt
def create_patient(request):         
    if request.method =='POST':

        staff_authenticate_serializer=AuthenticateStaffSerializer(data=request.data['staff'])
        # print(request.data)
        staff_authenticate_serializer.is_valid(raise_exception=True)          #Bad Request, 400 returned
        
        patient_serializer_for_branch=None

        if(staff_authenticate_serializer.authenticate_staff_function()):
            patient_serializer=PatientSerializer(data=request.data['patient'])
            if(patient_serializer.is_valid(raise_exception=True)):             #Bad Request, 400 returned
                # print(patient_serializer.save())
                
                if(request.data['staff']['branch']==request.data['patient']['branch']):
                    print("Right Patient Information")
                    patient_serializer_for_branch=PatientSerializer(patient_serializer.save()) #Serializing the object
                else:
                    return Response(staff_authenticate_serializer.errors,status=403)  #Unauthorized, 403 returned

            else:
                print("Wrong Patient Information")                             #Bad Request (Handled above)

        else:
            return Response(staff_authenticate_serializer.errors,status=401)  #Unauthenticated, 401 returned

        return Response(patient_serializer_for_branch.data,status=200)



# Patients List from Specific Branch
@api_view(['GET'])
def patient_list_specific_branch(request, branch_name):         
    if request.method == 'GET':
        all_patients_from_branch = Patient.objects.all().filter(branch=branch_name)
        patients_serializers = PatientSerializer(all_patients_from_branch, many=True) 
        return Response(patients_serializers.data, status=200)



# Patients Info
@api_view(['GET'])
def patient_info(request, patient_id):         
    if request.method == 'GET':
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist :
            return Response(status=404)
        patient_serializer = PatientSerializer(patient) 
        return Response(patient_serializer.data, status=200)