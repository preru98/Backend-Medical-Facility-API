from django.urls import path
from . import views

urlpatterns = [
    path('admins/', views.admin_list, name='admin_list'),
    path('branches/', views.branch_list, name='branch_list'),
    path('staff/', views.staff_list, name='staff_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
]
