from django.contrib import admin

# Register your models here.
from .models import ToDoItem

admin.site.register(ToDoItem)
