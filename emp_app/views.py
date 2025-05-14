from django.shortcuts import render,HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

def index(request):
    return render(request, 'emp_app/index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'emp_app/view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone_number = request.POST['phone']  # Maps to phone_number in model
        dept_id = int(request.POST['dept'])
        role_id = int(request.POST['role'])
        department = Department.objects.get(id=dept_id)
        role = Role.objects.get(id=role_id)
        
        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone_number=phone_number,
            department=department,
            role=role,
            hire_date=datetime.now(),
            location='Unknown'  # Optional: set location from POST if needed
        )
        new_emp.save()
        return HttpResponse('Employee Added Successfully')

    elif request.method == 'GET':
        return render(request, 'emp_app/add_emp.html')
    else:
        return HttpResponse("An Exception Occurred! Employee has not been added")


def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("employee removed successfuly")
        except:
            return HttpResponse("please enter a valid employee id ")
    emps = Employee.objects.all()
    return render(request, 'emp_app/remove_emp.html', {'emps': emps})
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()

        if name:
            # ✅ Use double underscores: __icontains
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        if dept:
            # ✅ Correct field name: department__name
            emps = emps.filter(department__name__icontains=dept)

        if role:
            # ✅ This one is correct
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, 'emp_app/view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'emp_app/filter_emp.html')

    else:
        return HttpResponse("An exception occurred.")
