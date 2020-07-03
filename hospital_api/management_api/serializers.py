from rest_framework import serializers
from management_api.models import Admin, Branch, Staff, Doctor, Patient

class AdminSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return Admin.objects.create(**validated_data)



class BranchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    discount_rate = serializers.FloatField()

    def create(self, validated_data):
        return Branch.objects.create(**validated_data)



class StaffSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=30)
    branch = serializers.ForeignKey(Branch, on_delete=serializers.CASCADE)
    password = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return Staff.objects.create(**validated_data)



class PatientSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=30)
    branch = serializers.ForeignKey(Branch, on_delete=serializers.CASCADE)
    age = serializers.PositiveIntegerField()

    def create(self, validated_data):
        return Patient.objects.create(**validated_data)



class DoctorSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)

    
