from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout  # Import the logout function
from .models import Employee
from .forms import LoginForm, EmployeeForm
from django.contrib import messages

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')  # Redirect after deletion

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Perform login logic
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):  # Custom logout view
    auth_logout(request)  # Log the user out
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # Redirect to the login page

def dashboard_view(request):
    return render(request, 'dashboard.html')

def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def create_employee_view(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        designation = request.POST.get('designation')
        gender = request.POST.get('gender')
        courses = request.POST.getlist('courses')  # Get selected courses
        image = request.FILES.get('image')

        # Validate email uniqueness
        if Employee.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('create_employee')

        # Validate mobile number
        if not mobile.isdigit():
            messages.error(request, "Mobile number must be numeric.")
            return redirect('create_employee')

        # Save Employee data
        Employee.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            designation=designation,
            gender=gender,
            course=', '.join(courses),  # Join selected courses into a string
            image=image
        )

        messages.success(request, "Employee created successfully!")
        return redirect('employee_list')  # Redirect to the employee list page

    return render(request, 'create_employee.html')


def edit_employee_view(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        designation = request.POST.get('designation')
        gender = request.POST.get('gender')
        courses = request.POST.getlist('courses')  # Get selected courses
        image = request.FILES.get('image')

        # Validate email uniqueness (ignore current employee)
        if Employee.objects.filter(email=email).exclude(id=employee.id).exists():
            messages.error(request, "Email already exists.")
            return redirect('edit_employee', employee_id=employee.id)

        # Validate mobile number
        if not mobile.isdigit():
            messages.error(request, "Mobile number must be numeric.")
            return redirect('edit_employee', employee_id=employee.id)

        # Update Employee data
        employee.name = name
        employee.email = email
        employee.mobile = mobile
        employee.designation = designation
        employee.gender = gender
        employee.course = ', '.join(courses)  # Join selected courses into a string
        
        if image:
            employee.image = image  # Only update image if a new one is provided

        employee.save()

        messages.success(request, "Employee updated successfully!")
        return redirect('employee_list')  # Redirect to the employee list page

    return render(request, 'edit_employee.html', {'employee': employee})
