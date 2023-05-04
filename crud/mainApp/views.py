from django.shortcuts import render,redirect
from .models import Employee

def home(Request):
    data = Employee.objects.all()
    return render(Request,'index.html',{'data':data})

def updateRecord(Request,id):
    data = Employee.objects.get(id=id)
    if (Request.method=="POST"):
        data.name = Request.POST.get('name')
        data.email = Request.POST.get('email')
        data.phone = Request.POST.get('phone')
        data.salary = Request.POST.get('salary')
        data.city = Request.POST.get('city')
        data.save()
        return redirect("/")
    return render(Request,'update.html',{'data':data})

def addRecord(Request):
    if (Request.method == "POST"):
        e = Employee()
        e.name = Request.POST.get('name')
        e.email = Request.POST.get('email')
        e.phone = Request.POST.get('phone')
        e.salary = Request.POST.get('salary')
        e.city = Request.POST.get('city')
        e.save()
        return redirect("/")
    return render(Request,'add.html')

def delete(Request,id):
    data = Employee.objects.get(id=id)
    if (data):
        data.delete()
    return redirect('/')