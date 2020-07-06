from django.urls import path
from . import views

urlpatterns = [
    path('admins/', views.admin_list, name='admin_list'),
    path('branches/', views.branch_list, name='branch_list'),
    path('staff/', views.staff_list, name='staff_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('login/staff/', views.staff_login, name='staff_login'),
    path('login/admin/', views.admin_login, name='admin_login'),
    path('login/doctor/', views.doctor_login, name='doctor_login'),
    path('branch/create/', views.create_branch, name='create_branch'),
    path('staff/create/', views.create_staff, name='create_staff'),
]
