"""employee_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
urlpatterns = [
    path('leave_application/',views.leave_application,name='leave_application'),
    path('manager_view/',views.manager_view,name="manager_view"),
    path('upadate_employee_status/<int:pk>/',views.upadate_employee_status,name="upadate_employee_status"),
     path('employee_status/<str:pk>/',views.employee_status,name="employee_status"),
]
