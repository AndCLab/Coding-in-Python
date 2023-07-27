from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from .models import ToDoItem

#Local Imports
from .models import ToDoItem 
from .forms import LoginForm, AddTaskForm, UpdateTaskForm, RegisterForm

def index(request):
	# todoitem_list = ToDoItem.objects.all()
	todoitem_list = ToDoItem.objects.filter(user_id=request.user.id)
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
	todoitem = get_object_or_404(ToDoItem,pk=todoitem_id)
	return render(request, "todolist/todoitem.html", model_to_dict(todoitem))


def register(request):
	context = {}

	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid() == False:
			form = RegisterForm()
		else:
			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			con_password = form.cleaned_data['con_password']
			hash_pass = make_password(password)
			user = authenticate(username=username, first_name=first_name, last_name=last_name, email=email, password=hash_pass)
			context = {
				"username": username,
				"first_name": first_name,
				"last_name": last_name,
				"email": email,
				"password": hash_pass,
			}
			
			duplicates = User.objects.filter(username=username)	

			if password == con_password:
				if not duplicates:
					User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=hash_pass)
					return redirect("todolist:login")
				else:	
					context = {
						"error": True
					}
			else:
				context = {
					"match": True
				}
	return render(request, "todolist/register.html", context)
	# users = User.objects.all()
	# is_user_unregistered = False
	# context = {
	# 	"is_user_unregistered": is_user_unregistered
	# }

	# for ind_user in users:
	# 	if(ind_user.username == "johndoe"):
	# 		is_user_unregistered = True
	# 		break

	# if is_user_unregistered == False:
	# 	user = User()
	# 	user.username = "johndoe"
	# 	user.first_name = "John"
	# 	user.last_name = "Doe"
	# 	user.email = "johndoe@mail.com"
	# 	# user.password = "john1234"
	# 	user.set_password('john1234')
	# 	user.is_staff = False
	# 	user.is_active = True
	# 	user.save()
	# 	context = {
	# 		"first_name": user.first_name,
	# 		"last_name": user.last_name
	# 	}
	# return render(request, "todolist/register.html", context)


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
	context = {}
	#If this is a POST request, we need to process form data
	if request.method == 'POST':
		#Create a form instance and populate it with data from the request
		form = LoginForm(request.POST)

		#Check whether the data is valid
		#Runs validation routines for all the form fields and returns True and places the form's data in the "cleaned_data" attribute
		if form.is_valid() == False:
			#Returns a blank login form
			form = LoginForm()

		else:
			#Retrieves the information from the form
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			context = {
				"username": username,
				"password": password
			}

		if user is not None:
			#Saves the user's ID in the session using Django's session framework
			login(request, user)
			return redirect("todolist:index")

		else:
			#Provides context with the error conditionally render the error message
			context = {
				"error": True
			}

	return render(request, "todolist/login.html", context)

def logout_view(request):
	logout(request)
	return redirect("todolist:index")

def add_task(request):
	context = {}
	if request.method == 'POST':
		form = AddTaskForm(request.POST)
		if form.is_valid() == False:
			form = AddTaskForm()
		else:
			task_name = form.cleaned_data['task_name']
			description = form.cleaned_data['description']
			#Checks the database if a task already exists
			#By default the filter method searches for records that are case insensitive
			duplicates = ToDoItem.objects.filter(task_name=task_name)	

			#If todoitem does not contain any duplicates
			if not duplicates:
				#creates an object based on the "ToDoItem" model and saves the record in the database
				ToDoItem.objects.create(task_name=task_name, description=description, date_created=timezone.now(), user_id=request.user.id)
				return redirect("todolist:index")
			else:
				context = {
					"error": True
				}
	return render(request, "todolist/add_task.html", context)

def update_task(request, todoitem_id):
	# Returns a queryset
	todoitem = ToDoItem.objects.filter(pk=todoitem_id)
	context = {
		"user": request.user,
		"todoitem_id": todoitem_id,
		# Accessing the first element is necessary because the "ToDoItem.objects.filter()" method returns a queryset
		"task_name": todoitem[0].task_name,
		"description": todoitem[0].description,
		"status": todoitem[0].status
	}
	if request.method == 'POST':
		form = UpdateTaskForm(request.POST)
		if form.is_valid() == False:
			form = UpdateTaskForm()

		else:
			task_name = form.cleaned_data['task_name']
			description = form.cleaned_data['description']
			status = form.cleaned_data['status']

			if todoitem:
				todoitem[0].task_name = task_name
				todoitem[0].description = description
				todoitem[0].status = status

				todoitem[0].save()
				return redirect("todolist:index")

			else:
				context = {
					"error": True
				}
	return render(request, "todolist/update_task.html", context)

def delete_task(request, todoitem_id):
	todoitem = ToDoItem.objects.filter(pk=todoitem_id).delete()
	return redirect("todolist:index")