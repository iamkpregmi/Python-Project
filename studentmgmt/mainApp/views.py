from django.shortcuts import render
from .models import student

def home(request):
    return render(request,"index.html")

def register(request):
    if request.method == "POST":
        rollno = request.POST.get("rollno","Null")
        name = request.POST.get("name","User")
        fee = request.POST.get("fee","0.00")
        sd = student(roll_no=rollno,name=name,fee=fee)
        sd.save()
        mydata={
            "msg":"Register Successfully" 
        }
        return render(request,"register.html",mydata)
    return render(request,"register.html")


