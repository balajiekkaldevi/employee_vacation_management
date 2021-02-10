from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import io

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import employee,manager,days
from .serializer import employeeserializer,managerserialiazer,daysserialiazer
from rest_framework.decorators import api_view
@api_view(['GET'])
def manager_view(request):
    if request.method =='GET':
        em=employee.objects.filter(status="Pending")
        w=employeeserializer(em,many=True)
        d=days.objects.all()
        dm=daysserialiazer(d,many=True)
        for i in w.data:
            if(i['status']=='Pending'):
                for j in dm.data:
                    if(i['emp_id']==j['e']):
                        i['total_leaveas_before_taken']=j['day']
    
                        
        return Response(w.data)
@api_view(['PATCH','GET'])    
def upadate_employee_status(request,pk):
    if request.method=='PATCH':
        try:
            w=employee.objects.get(emp_id=pk,status='Pending')
            se=employeeserializer(instance=w,data=request.data,partial=True)
            if se.is_valid():
                se.save()
                i=se.data
                d=days.objects.get(e=pk)
                dm=daysserialiazer(d) 
                j=dm.data
                if(i['status']=='Approved'):
                    w=j['day']+i['no_of_days']
                    d=days.objects.get(e=pk)
                    dm=daysserialiazer(instance=d,data={'day':'{}'.format(w)},partial=True) 
                    if dm.is_valid():
                        dm.save()
                
                        return Response(dm.data)
        except employee.DoesNotExist:
            return Response("Employee doesn't exist")
        

    return Response({"Employee":"see updated status"})

@api_view(['POST','GET'])
def leave_application(request):

    se=employeeserializer(data=request.data)
    if se.is_valid():
        se.save()
        s=days.objects.all()
        sa=daysserialiazer(s,many=True)
        for j in sa.data:
            if j['e']==se.data['emp_id']:
                if(j['day']>=30):
                    return Response({"Your application was rejected"})
                return Response(sa.data)
            
        dm=daysserialiazer(data={'e':'{}'.format(se.data['emp_id']),'day':0})
        if(dm.is_valid()):
            dm.save()
            return Response(dm.data)
    return Response(se.data)

@api_view(['GET'])
def employee_status(request,pk=None):
    if request.method=='GET' and pk is not None:
        em=employee.objects.all()
        w=employeeserializer(em,many=True)
        for i in w.data:
            if str(i['emp_id'])==pk and i['status']=='Pending':
                return Response(i)
        return Response({'emp_id':'{}'.format(pk),'status':'Approved'})
    return Response({"Please enter valid employee id"})
   
