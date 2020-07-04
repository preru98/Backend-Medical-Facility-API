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
    # username = serializers.CharField(max_length=200)
    # email = serializers.EmailField()
    # phone_number = serializers.CharField(max_length=30)
    # password = serializers.CharField(max_length=15)
    # branch = serializers.CharField()

#     def create(self, validated_data):
#         branch_id=validated_data['branch']
#         get_branch=Branch.objects.get(pk=branch_id)
#         new_validated_data={
#             'branch' : get_branch,
#             'username' : validated_data['username'],
#             'email' : validated_data['email'],
#             'phone_number' : validated_data['phone_number'],
#             'password' : validated_data['password'],
#         }
#         new_staff= Staff.objects.create(**new_validated_data)
#         new_staff.save()
#         return new_staff
        


# class PatientSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=200)
#     email = serializers.EmailField()
#     phone_number = serializers.CharField(max_length=30)
#     age = serializers.IntegerField(min_value=0)
#     branch = serializers.IntegerField()

#     def create(self, validated_data):
#         return Patient.objects.create(**validated_data)



# class DoctorSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=200)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=15)

#     def create(self, validated_data):
#         return Doctor.objects.create(**validated_data)

    
