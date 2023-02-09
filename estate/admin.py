from django.contrib import admin
from .models import House, Agents, Profile

# Register your models here.

admin.site.register(House) 
admin.site.register(Agents)
admin.site.register(Profile)
