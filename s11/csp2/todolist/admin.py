from django.contrib import admin

# Register your models here.
from .models import ToDoItem, Event

admin.site.register(ToDoItem)
admin.site.register(Event)