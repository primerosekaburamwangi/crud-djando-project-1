from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from myapp.forms import EmployeeForm
from myapp.models import Employee


def createEmp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show")
    else:
        form = EmployeeForm()
    return render(request, "index.html", {"form": form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {"employees": employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {"employee": employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {"employee": employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
