from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.forms.models import model_to_dict

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from .models import ToDoItem

# Create your views here.

def index(request):
	todoitem_list = ToDoItem.objects.all()
	context = {
		'todoitem_list': todoitem_list,
		'user': request.user
	}
	return render(request, "todolist/index.html", context)
	# template = loader.get_template("todolist/index.html")
	# context = {
	# 	'todoitem_list': todoitem_list
	# }
	# return HttpResponse(template.render(context, request))

	# output = ', '.join([todoitem.task_name for todoitem in todoitem_list])
	# return HttpResponse(output)

	# return HttpResponse('Hello from the views.py file')

def todoitem(request, todoitem_id):
	todoitem = model_to_dict(ToDoItem.objects.get(pk=todoitem_id))
	return render(request, "todolist/todoitem.html", todoitem)


def register(request):
	users = User.objects.all()
	is_user_registered = False
	context = {
		"is_user_registered": is_user_registered
	}

	for ind_user in users:
		if(ind_user.username == "johndoe"):
			is_user_registered = True
			break

	if is_user_registered == False:
		user = User()
		user.username = "johndoe"
		user.first_name = "John"
		user.last_name = "Doe"
		user.email = "johndoe@mail.com"
		# user.password = "john1234"
		user.set_password('john1234')
		user.is_staff = False
		user.is_active = True
		user.save()
		context = {
			"first_name": user.first_name,
			"last_name": user.last_name
		}
	return render(request, "todolist/register.html", context)

def change_password(request):
	is_user_authenticated = False
	user = authenticate(username="johndoe", password="john1234")
	print(user)
	if user is not None:
		authenticated_user = User.objects.get(username="johndoe")
		authenticated_user.set_password("johndoe1")
		authenticated_user.save()
		is_user_authenticated = True
	context = {
		"is_user_authenticated": is_user_authenticated
	}
	return render(request, "todolist/change_password.html", context)

def login_view(request):
	username = "johndoe"
	password = "johndoe1"
	user = authenticate(username=username, password=password)
	print(user)
	if user is not None:
		login(request, user)
		return redirect("index")
	else:
		context = {"is_user_authenticated": False}
		return render(request, "todolist/login.html", context)

def logout_view(request):
	logout(request)
	return redirect("index")
