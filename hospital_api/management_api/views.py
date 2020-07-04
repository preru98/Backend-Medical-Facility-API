from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from management_api.models import Admin, Branch, Staff, Doctor, Patient
from management_api.serializers import AdminSerializer, BranchSerializer, StaffSerializer
# , DoctorSerializer, PatientSerializer

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