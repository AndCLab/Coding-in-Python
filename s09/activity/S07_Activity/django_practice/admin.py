from django.contrib import admin

# Register your models here.
from .models import GroceryItems

admin.site.register(GroceryItems)