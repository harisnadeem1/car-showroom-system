from django.shortcuts import render, redirect

from admin_portal.models import Car, CarImage, Subscribe, Buyer, Status

def index(request):
    
    cars = Car.objects.all()
    c = []
    n = 0
    for j in cars:
        c.append(j)
        n = n+1
        if n == 3:
            break
    d = []

    for i in c:
        images = CarImage.objects.filter(car_id=i.car_id).first()
        d.append([i, images])
    
    companies = Car.objects.values("company").distinct()
    
    for i in companies:
        print(i)
    
    data = {
        'cars_header' : d,
        'companies': companies
    }
    
    return render(request, 'index.html', context=data)


def subscribe(request):
    if request.method == "POST":
        email = request.POST["email"]
        s = Subscribe()
        s.email = email
        s.save()
        
    return redirect("/")


def vehicle(request):
    company = request.GET["company"]
    car = []
    if company == "all":
        cars = Car.objects.all()
        for i in cars:
            images = CarImage.objects.filter(car_id=i.car_id).first()
            car.append([i, images])
    else:
        cars = Car.objects.filter(company=company)
        for i in cars:
            images = CarImage.objects.filter(car_id=i.car_id).first()
            car.append([i, images])
            
    data = {
        "cars":car,
    }
    
    return render(request, "models.html", context=data)


def car(request):
    id = request.GET["id"]
    _car = Car.objects.get(car_id=id)
    images = CarImage.objects.filter(car_id=id)
    
    
    data = {
        'car':_car,
        'images':images
    }
    return render(request, "car.html", context=data)

def buy(request):
    if request.method == "POST":
        id = request.POST["id"]
        fname = request.POST["full_name"]
        contact = request.POST["contact"]
        address = request.POST["address"]
        method = request.POST["method"]
        
        car = Car.objects.get(car_id=id)
        buy = Buyer()
        status = Status.objects.get(status_id=1)
        buy.buyer_name = fname
        buy.buyer_address = address
        buy.buyer_contact = contact
        buy.buyer_payment_method = method
        buy.car_id = car
        buy.status = status
        buy.save()
        
        return redirect("/")
    
    id = request.GET["id"]
    data = {
        'id' : id
    }
    return render(request, "buy.html", context=data)

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")