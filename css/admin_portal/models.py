from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import uuid, os
# Create your models here.

def unique_car_image(instence, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("cars", filename)

class Car(models.Model):
    car_id = models.AutoField(primary_key=True ,null=False)
    user_id = models.ForeignKey(User, on_delete=CASCADE, related_name="users_cars")
    car_name = models.CharField(max_length=100, null=False)
    car_model = models.CharField(max_length=100, null=False)
    car_price = models.IntegerField(null=True)
    company = models.CharField(max_length=100, null=False)
    status = models.BooleanField(null=False)
    description = models.TextField(max_length=2500, null=False)

    def __str__(self):
        return self.car_name + "-" + self.car_model
    
class CarImage(models.Model):
    image_id = models.AutoField(primary_key=True, null=False)
    car_id = models.ForeignKey(Car, on_delete=CASCADE, related_name="images_of_cars")
    image = models.ImageField(upload_to=unique_car_image, null=False)

    def __str__(self):
        return str(self.car_id)

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.status

class Buyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    buyer_name= models.CharField(max_length=50)
    buyer_address = models.CharField( max_length=50)
    buyer_contact = models.CharField(max_length=50)
    buyer_payment_method = models.CharField( max_length=50)
    car_id = models.ForeignKey(Car, verbose_name=("buy_car"), on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name="order_status", on_delete=CASCADE)
    
    def __str__(self):
        return str(self.buyer_id) + " > " + self.buyer_name + " - (" + self.car_id.car_name + " - " + self.car_id.car_model + ")"
    
class Subscribe(models.Model):
    sub_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=70)
    
    def __str__(self):
        return self.email
    
