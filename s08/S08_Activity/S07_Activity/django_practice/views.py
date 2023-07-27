from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import GroceryItems 

def index(request):
	groceryitem_list = GroceryItems.objects.all()
	template = loader.get_template("django_practice/index.html")
	context = {
		'groceryitem_list': groceryitem_list
		}
	return HttpResponse(template.render(context, request))
	# output = ', '.join([groceryitem.item_name for groceryitem in groceryitem_list])
	# return HttpResponse(output)
	# return HttpResponse("Hello from the views.py file")

def groceryitem(request, groceryitem_id):
	response = "You are viewing the details of %s"
	return HttpResponse(response % groceryitem_id)

	