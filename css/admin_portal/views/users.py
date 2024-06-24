from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

@login_required(login_url='/')
def user(request):
    if request.method == "POST":
        user = request.POST["user"]
        User.objects.get(username=user).delete()
        messages.success(request, "User Deleted Successfully!")  
        
    users = User.objects.all()

    data = {
        "users":users
    }
    return render(request, "_admin/users.html", context=data)

@login_required(login_url='/')
def adduser(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        type = request.POST["type"]
        
        user = User()
        user.username = username
        user.first_name=fname
        user.last_name=lname
        user.email=email
        user.set_password(password)
        if type == "1":
            user.is_staff = True
        elif type == "2":
            user.is_staff = True
            user.is_superuser = True
    
        user.save()
        messages.success(request, "User Added Successfully!")       
         
    return render(request, "_admin/adduser.html")