from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class House(models.Model):

    buy = 'by'
    sale = 'sl'
    rent = 'rt'

    office_space = 'os'
    apartment = 'ap'
    house = 'hs'

    status_choices = [
    (buy,'buy'), (sale,'sale'), (rent,'rent')
    ]
    item_listing_type = [
    (office_space,'office space'), (apartment,'apartment'), (house,'house')
    ]

    
    name = models.CharField(default = None, max_length=70)
    address = models.CharField(default = None, max_length=150)
    description = models.TextField(default = None,)
    price = models.FloatField(default = None,)
    image = models.ImageField(upload_to = 'static/images')
    bed_rooms = models.PositiveIntegerField(null = True)
    living_rooms = models.PositiveIntegerField(null = True)
    parking = models.PositiveIntegerField(null = True)
    kitchen = models.PositiveIntegerField(null = True)
    status = models.CharField(max_length= 2, choices=status_choices, default=rent) 
    listing = models.CharField(max_length= 2,choices=item_listing_type, default=apartment)
    added = models.DateTimeField(auto_created=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"House: {self.name} at address: {self.address}"

class Agents(models.Model):
    
    name = models.CharField( max_length=80)
    phone_number = models.IntegerField(blank=True)
    email = models.EmailField( max_length=254)
    image = models.ImageField( upload_to='static/images')

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='static/images', null= True)
    
    def __str__(self):
        return self.agent.name