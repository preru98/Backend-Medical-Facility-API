from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from management_api.models import Admin, Branch, Staff, Doctor, Patient
from management_api.serializers import AdminSerializer, BranchSerializer, StaffSerializer, DoctorSerializer, PatientSerializer

# Create your views here.

#List of Registered Admin
def admin_list(request):
    if request.method == 'GET':
        allAdmins = Admin.objects.all()
        serializer = AdminSerializer(allAdmins, many=True)
        return JsonResponse(serializer.data, safe=False)



#List of Registered Staff
def staff_list(request):
    if request.method == 'GET':
        allStaff = Staff.objects.all()
        serializer = StaffSerializer(allStaff, many=True)
        return JsonResponse(serializer.data, safe=False)    



#List of Registered Branch
def branch_list(request):
    if request.method == 'GET':
        allBranches = Branch.objects.all()
        serializer = BranchSerializer(allBranches, many=True)
        return JsonResponse(serializer.data, safe=False)



#List of Registered Patients
def patient_list(request):
    if request.method == 'GET':
        allPatients = Patient.objects.all()
        serializer = PatientSerializer(allPatients, many=True)
        return JsonResponse(serializer.data, safe=False)



#List of Registered Doctors
def doctor_list(request):
    if request.method == 'GET':
        allDoctors = Doctor.objects.all()
        serializer = DoctorSerializer(allDoctors, many=True)
        return JsonResponse(serializer.data, safe=False)



#Staff Login
@csrf_exempt
def staff_login(request):
    if request.method =='POST':
        data=JSONParser().parse(request)
        login_username=data['username']
        login_password=data['password']
        try:
            staff_member=Staff.objects.get(username=login_username)
            print(staff_member.id)

        except Staff.DoesNotExist:
            print("Caught")
            return HttpResponse(status=404)
        
        if(staff_member.password==login_password):
            responseDict={
                'Authentication':True,
            }
        else:
            responseDict={
                'Authentication':False,
            }
        return JsonResponse(responseDict,status=200)



#Admin Login
@csrf_exempt
def admin_login(request):
    if request.method =='POST':
        data=JSONParser().parse(request)
        login_username=data['username']
        login_password=data['password']
        try:
            current_admin=Admin.objects.get(username=login_username)

        except Admin.DoesNotExist:
            print("Caught")
            return HttpResponse(status=404)
        
        if(current_admin.password==login_password):
            responseDict={
                'Authentication':True,
            }
        else:
            responseDict={
                'Authentication':False,
            }
        return JsonResponse(responseDict,status=200)



#Doctor Login
@csrf_exempt
def doctor_login(request):
    if request.method =='POST':
        data=JSONParser().parse(request)
        login_username=data['username']
        login_password=data['password']
        try:
            current_doctor=Doctor.objects.get(username=login_username)

        except Doctor.DoesNotExist:
            print("Caught")
            return HttpResponse(status=404)
        
        if(current_doctor.password==login_password):
            responseDict={
                'Authentication':True,
            }
        else:
            responseDict={
                'Authentication':False,
            }
        return JsonResponse(responseDict,status=200)