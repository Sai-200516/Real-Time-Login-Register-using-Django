from django.shortcuts import render
from django.http import HttpResponse
from demoapp.models import Customer
from demoapp.models import Auth

def login(request):
    if request.method=="POST":
        Email=request.POST["Email"]
        Password=request.POST["Password"]
        #Post_1=Auth.objects.values()
        users=Auth.objects.all().values("Email","Password")
        #if Email in Auth.objects.values_list("Email",flat=True):
        if Email in users:
            #if Password in Auth.objects.values_list("Password",flat=True):
            if Password in users:
                Post_1=Auth.objects()
                #messages.success(request,'Logged in Successfully!!!')
                #return render(request,"index.html",{'post':users})
                return HttpResponse("Login Sucess")
            else:
                #return render(request,"login.html")
                #messages.error(request,'Invalid Credentials!!!')
                return HttpResponse("Login password fail")
        else:
            return HttpResponse("Login fail")
            #return render(request,"login.html")
            #messages.error(request,'Invalid Credentials!!!')
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def index(request):
    Post=Customer.objects.all()
    Post_1=Auth.objects.all()
    return render(request,"index.html",{"name":"Appikonda Sai","post":Post_1})
def signup(request):
    if request.method=="POST":
        """if 'Name'in request.POST:
            Name=request.POST["Name",""]
        else:
            return HttpResponse("NAME IS NOT THERE")"""
        Name=request.POST["Name"]
        #Created_at=request.POST["Created_at"]
        Email=request.POST["Email"]
        Password=request.POST["Password"]
        Dob=request.POST["Dob"]
        Image=request.FILES.get("Image")

        """k=Customer(Name=Name,Created_at=Created_at,Image=Image)
        k.save()"""
        if Auth.objects.filter(Email=Email).exists():
            return HttpResponse("User already exit")
        else:
            a=Auth(Name=Name,Email=Email,Password=Password,Dob=Dob,Image=Image)
            a.save()

        return render(request,"login.html")
    return render(request,"signup.html")
def logout(request):
    return render(request,"login.html")