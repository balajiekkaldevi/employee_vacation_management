from rest_framework import serializers
from .models import employee,manager,days
from django.utils import timezone
import datetime
class employeeserializer(serializers.Serializer):
    emp_id=serializers.IntegerField()
    emp_name=serializers.CharField(max_length=100)
    vac_start=serializers.DateField()
    vac_end=serializers.DateField()
    no_of_days=serializers.IntegerField()
    created_at=serializers.DateTimeField(default=timezone.now)
    status=serializers.CharField(default='Pending',max_length=20)
    def create(self, validated_data):
        return employee.objects.create(**validated_data)

    def update(self,instance, validated_data):
        self.instance.status = self.validated_data.get('status', instance.status)
        self.instance.save()
        return self.instance
    

    
class managerserialiazer(serializers.Serializer):
    m_id=serializers.IntegerField()
    m_name=serializers.CharField(max_length=100)

    
class daysserialiazer(serializers.Serializer):
    e=serializers.IntegerField()
    day=serializers.IntegerField()
    
    def update(self,instance, validated_data):
        self.instance.day = self.validated_data.get('day', instance.day)
        self.instance.save()
        return self.instance

    def create(self, validated_data):
        return days.objects.create(**validated_data)
    
    
'''
    
class statusserializer(serializers.Serializer):
    emp_id=serializers.IntegerField()
    emp_name=serializers.CharField(max_length=100)
    vac_start=serializers.DateField()
    vac_end=serializers.DateField()
    no_of_days=serializers.IntegerField()
    created_at=serializers.DateTimeField(default=timezone.now)
    status=serializers.CharField(default='Pending',max_length=20)

    def create(self, validated_data):
        return status.objects.create(**validated_data)'''
