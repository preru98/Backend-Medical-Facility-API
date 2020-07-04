from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_list, name='admin_list'),
    path('branch/', views.branch_list, name='branch_list'),
    # path('staff/', views.staff_list, name='staff_list'),
]
