

# Create your models here.
from django.db import models

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profiles/')
    portfolio_url = models.URLField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.photographer.name} by {self.customer_name}"
    


# Create your models here.
class Contact(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=30)
    mobile=models.CharField(max_length=12)
    contact=models.CharField(max_length=300)
    date=models.DateField()
def _str_(self):
    return self.mobile

class Photographer1(models.Model):
    fullname=models.CharField(max_length=70)
    email=models.EmailField(max_length=30)
    mobile=models.CharField(max_length=12)
    password=models.CharField(max_length=15)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=30)
    yourworks=models.CharField(max_length=200)

class Cuslogin(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=15)
    
















































