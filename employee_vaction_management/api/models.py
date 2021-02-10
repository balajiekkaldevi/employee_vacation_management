from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

    
class manager(models.Model):
    m_id=models.IntegerField()
    m_name=models.CharField(max_length=100)

   
class employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=100)
    vac_start=models.DateField()
    vac_end=models.DateField()
    no_of_days=models.IntegerField()
    created_at=models.DateTimeField(default=timezone.now)
    status=models.CharField(default='Pending',max_length=20)


class days(models.Model):
    e=models.IntegerField()
    day=models.IntegerField()



'''class status(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=100)
    vac_start=models.DateField()
    vac_end=models.DateField()
    no_of_days=models.IntegerField()
    created_at=models.DateTimeField(default=timezone.now)
    status=models.CharField(default='Pending',max_length=20)'''