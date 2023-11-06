from django.shortcuts import render,HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    
    return render(request,'index.html')


def all_emp(request):
    
    # To view All items in the Model using Django QuerySet - modelname.objects.all()
    
    emps = Employee.objects.all()
    
    context = {
        'emps':emps
    }
    
    return render(request, 'all_emp.html',context)

def add_emp(request):
    
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = eval(request.POST.get('department'))
        salary = eval(request.POST.get('salary'))
        bonus = eval(request.POST.get('bonus'))
        role = eval(request.POST.get('role'))
        phone = eval(request.POST.get('phone'))
        
        new_emp = Employee(first_name=first_name,last_name=last_name,dept_id=department,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.now())
        new_emp.save()
        
        
        return render(request,'add_emp.html',{'details':True})
    
    elif request.method == 'GET':
        
        return render(request,'add_emp.html')

def remove_emp(request,emp_id = 0):
    
    if emp_id:
        try:
            emp_to_rm = Employee.objects.get(id=emp_id)
            emp_to_rm.delete()
            
            return render(request,'remove_emp.html',{'rmd':True})
        
        except:
            
            return HttpResponse("Can not remove the Employee")
            
    emps = Employee.objects.all()
    
    context = {
        'emps':emps
    }

    return render(request,'remove_emp.html',context)

def filter_emp(request):
    
    if request.method == 'POST':
        
        name = request.POST.get('name')
        dept = request.POST.get('department')
        role = request.POST.get('role')
        
        emps = Employee.objects.all()
        
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
            
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
            
        if role:
            emps = emps.filter(role__name__icontains = role)
            
        context = {
            'emps':emps
        }
    
        return render(request,'view_all_emp.html',context)
    
    elif request.method == 'GET':
        
        return render(request,'filter_emp.html')