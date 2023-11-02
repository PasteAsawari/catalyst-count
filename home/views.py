from django.shortcuts import render,HttpResponse,redirect
from home.models import Company,File
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import pandas as pd
from django.template import loader
#import os
# Create your views here.

def index(request):
    #return HttpResponse("This is my home page")
    return render(request,"index.html")

def addup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname= request.POST["fname"]
        lname= request.POST["lname"]
        email= request.POST["email"]
        pass1= request.POST["pass1"]
        pass2 = request.POST["pass2"]

        #check for errorneous input
        if len(username)>10:
            messages.error(request,"username must be under 10 characters")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,"username should contain characters and numbers")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request,"Passwords are not matching")
            return redirect('home')

        #create a user
        newuser = User.objects.create_user(username,email,pass1)
        newuser.first_name = fname
        newuser.last_name = lname
        newuser.save()
        messages.success(request,"New User has been added!")
        return redirect('users')

    else:
        return HttpResponse("404-Not Found")



def upload_csv_data_db(file_path):
    df = pd.read_csv(file_path)
    print(df.values)
    list_of_csv = [list(row) for row in df.values]
    print(list_of_csv)
    for l in list_of_csv:
        Company.objects.create(
            name= l[0],
            domain= l[1],
            year_founded=l[2],
            industry=l[3],
            size_range=l[4],
            locality=l[5],
            country=l[6],
            linkedin_url= l[7],
            current_employee_estimate=l[8],
            total_employee_estimate= l[9])

    

def uploaddata(request):
    if request.method =="POST":
        myfile= request.FILES['file']
        obj=File.objects.create(file=myfile)
        print(obj.file)
        upload_csv_data_db(obj.file)

    return render(request,"uploaddata.html")
    #return HttpResponse("This is my upload Data page")

def manageLogin(request):
    if request.method=="POST":
        loginusername = request.POST["loginusername"]
        loginpassword= request.POST["pass"]

        user= authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully logged in!")
            return redirect('home')
        else:
            messages.error(request,"Please enter valid credentials!")
            return redirect('home')
    return HttpResponse("404- Not found")

def manageLogout(request):
    logout(request)
    messages.success(request,"Successfully logged out!")
    return redirect('home')


def querybuilder(request):
    #return HttpResponse("This is my querybuilder page")
    #uerydata =Company.objects.all().values()
    uerydata =Company.objects.order_by().values('industry').distinct() 
    years=Company.objects.order_by().values('year_founded').distinct() 
    localities = Company.objects.order_by().values('locality').distinct()
    company_names = Company.objects.order_by().values('name').distinct()
    template = loader.get_template('querybuilder.html')
    context = {
        'members':uerydata,
        'years':years,
        'localities': localities,                       
        'company_names':company_names
    }
    #return render(request,"querybuilder.html")
    return HttpResponse(template.render(context,request))

def users(request):
    #records = User.objects.all().values()
    #print(records)
    #return render(request,'users.html',{'records':records})
    mydata = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
    'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))
  


