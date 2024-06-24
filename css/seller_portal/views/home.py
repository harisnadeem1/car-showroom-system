from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as _logout
from django.contrib.auth import login as _login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from admin_portal.models import Car, CarImage, Buyer, Status
from django.contrib.auth.models import User

@login_required(login_url="/seller/login/")
def index(request):
    
    cars = Car.objects.filter(user_id=request.user)
    d = []
    for i in cars:
        images = CarImage.objects.filter(car_id=i.car_id).first()
        d.append([i, images])
    data = {
        'cars' : d
    }
    
    return render(request, 'seller/index.html', context=data)

def login(request):
    if request.method == "POST":
        user = request.POST["user"]
        password = request.POST["password"]
        user = authenticate(username=user, password=password)
        if user is not None:
            us = User.objects.filter(username=user)
            for i in us:
                if i.is_staff:
                    _login(request, user)
                    return redirect("/seller/")
            
            messages.error(request, "Incorrect Username Or Passowrd!")
            return render(request, '_admin/login.html')
        else:
            messages.error(request, "Incorrect Username Or Passowrd!")
            return render(request, '_admin/login.html')

    return render(request, "seller/login.html")

@login_required(login_url="/seller/login/")
def car(request):
    if request.method == "POST":
        id = request.POST["id"]
        CarImage.objects.filter(car_id=id).delete()
        Car.objects.get(car_id=id).delete()
        return redirect("/seller/")
    
    id = request.GET["id"]
    _car = Car.objects.get(car_id=id)
    images = CarImage.objects.filter(car_id=id)
    
    
    data = {
        'car':_car,
        'images':images
    }
    
    return render(request, "seller/car.html", context=data)

@login_required(login_url="/seller/login/")
def editcar(request):
    if request.method == "POST":
        id = request.POST["id"]
        car_name= request.POST["car_name"]
        company= request.POST["company"]
        price= request.POST["price"]
        description= request.POST["desc"]
        
        ob = Car.objects.get(car_id=id)
        ob.car_name = car_name
        ob.company = company
        ob.car_price = price
        ob.description = description
        
        ob.save()
        
        return redirect("/seller/")
    
    id = request.GET["id"]
    car = Car.objects.get(car_id=id)
    data = {
        'car':car
    }
    return render(request, "seller/editcar.html", context=data)

@login_required(login_url="/seller/login/")
def addcar(request):
    if request.method == "POST":
        company = request.POST["company"]
        car_name= request.POST["car_name"]
        description= request.POST["description"]
        price = request.POST["price"]
        image = request.FILES['image']
        car_model = request.POST["car_model"]
        
        new_car = Car.objects.create(company=company, car_name=car_name, description= description, car_price=price, status=True, user_id=request.user)
        new_car.car_model = car_model
        new_car.save()
        
        img = CarImage()
        img.car_id=new_car
        img.image=image
        img.save()
        
        img = CarImage()
        img.car_id=new_car
        img.image=request.FILES['image2']
        img.save()
        
        img = CarImage()
        img.car_id=new_car
        img.image=request.FILES['image3']
        img.save()
        
        messages.error(request, "Car Added Successfully!")
        
    return render(request, 'seller/addcar.html')

@login_required(login_url="/seller/login/")
def orders(request):
    if request.method == "POST":
        status_id = request.POST["status_id"]
        buyer_id = request.POST["buyer_id"]
        
        buyer = Buyer.objects.get(buyer_id=buyer_id)
        status = Status.objects.get(status_id=status_id)
        buyer.status = status
        buyer.save()
        messages.error(request, "Status Updated Successfully.")
        
    cars = Car.objects.filter(user_id=request.user)
    orders = []
    for i in cars:
        order = Buyer.objects.filter(car_id=i)
        for j in order:
            orders.append(j)
    stat = Status.objects.all()
    data = {
        "orders":orders,
        "status":stat
    }
    
    return render(request, 'seller/order.html', data)