from rest_framework import serializers
from management_api.models import Admin, Branch, Staff, Doctor, Patient

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'username', 'email', 'password']



class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'discount_rate']



class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'username', 'email', 'phone_number', 'password', 'branch']
        


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'username', 'email', 'phone_number', 'age', 'branch']



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'username', 'email', 'password']

    

class AuthenticateAdminSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True, required=False)
    username = serializers.CharField(max_length=200, required=False)

    def authenticate_admin_function(self):
        try:
            current_admin=Admin.objects.get(email=self.validated_data['email'])
        except Admin.DoesNotExist:
            print("Caught")
            return False

        if(current_admin.password==self.validated_data['password']):
            return True
        return False

    class Meta:
        model = Admin
        fields = ['id', 'username', 'email', 'password']
    

