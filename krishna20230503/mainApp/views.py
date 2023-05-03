from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def form(request):
    return render(request,"form.html")

def result(request):
    if request.method == "GET":
        data = request.GET.get("text","Null")
        
        #Logical code implement here
        lcv = 0
        lcc = 0
        ucv = 0
        ucc = 0
        sp = 0
        digit = 0
        special = 0
        for i in data:
            if (i>='a' and i<='z'):
                if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
                    lcv+=1
                else:
                    lcc += 1
            elif (i>='A' and i<="Z"):
                if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                    ucv+=1
                else:
                    ucc += 1
            elif (i>='0' and i<='9'):
                digit += 1
            elif (i==' '):
                sp += 1
            else:
                special += 1
        data = {
            "lcv" : lcv,
            "lcc" : lcc,
            "ucv" : ucv,
            "ucc" : ucc,
            "sp" : sp,
            "digit" : digit,
            "special" : special,
        }
    return render(request,"result.html",data)

def about(request):
    return render(request,"about.html")