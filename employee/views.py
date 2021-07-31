from django import forms
from .forms import Employeeform
from django.shortcuts import redirect, HttpResponseRedirect,render
from .models import Employee


# Create your views here.
def emplist(request):
    context={'employee_list':Employee.objects.all()}
    
    return render(request,'employee_list.html',context)

def employee_form(request,id=0):
    
    if request.method=="GET":
        if id==0:
            res=Employeeform()
        else:
            employee=Employee.objects.get(pk=id)
            res=Employeeform(instance=employee)
        return render(request,'employee_form.html',{'form':res})
    else:
        if id ==0:
            res=Employeeform(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            res=Employeeform(request.POST,instance=employee)
        if res.is_valid():
            res.save()
        return HttpResponseRedirect('list/')



def delete(request,id):
    emp=Employee.objects.get(pk=id)
    emp.delete()

    return HttpResponseRedirect('list/')
