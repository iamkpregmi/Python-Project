from django.shortcuts import render
from .models import myToDoList

def home(request):
    try:
        if request.method == "POST":
            output = str(request.GET.get("new"))
            print(output)

        mydata = myToDoList.objects.all()
        data = {
            "data": mydata
        }
    except:
        pass
    return render(request,"index.html",data)