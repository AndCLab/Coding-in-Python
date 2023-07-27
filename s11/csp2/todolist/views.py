from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.forms.models import model_to_dict
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils import timezone

#Local Imports
from .models import ToDoItem, Event 
from .forms import LoginForm, AddTaskForm, AddEventForm, UpdateTaskForm, RegisterForm, UpdateProfileForm

def index(request):
	todoitem_list = ToDoItem.objects.filter(user_id=request.user.id)
	event_list = Event.objects.filter(user_id=request.user.id)
	context = {
		'todoitem_list': todoitem_list,
		'event_list': event_list,
		'user': request.user
	}
	return render(request, "todolist/index.html", context)

def todoitem(request, todoitem_id):
	todoitem = get_object_or_404(ToDoItem,pk=todoitem_id)
	return render(request, "todolist/todoitem.html", model_to_dict(todoitem))

def eventitem(request, eventitem_id):
	eventitem = get_object_or_404(Event,pk=eventitem_id)
	return render(request, "todolist/eventitem.html", model_to_dict(eventitem))

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

@login_required
def update_profile(request, user_id):
	user = get_object_or_404(User, id=user_id)
	if request.method == 'POST':
		form = UpdateProfileForm(request.POST, instance=user)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			password = form.cleaned_data['password']
			
			if password != '':
				user.password = make_password(form.cleaned_data['password'])
			else:
				user.password = request.user.password

			form.save()
			return redirect('todolist:index')
	else:
		form = UpdateProfileForm(instance=user)

	context = {
		"user_id": user_id,
		"user": user,
		"form": form
	}
	return render(request, 'todolist/update_profile.html', context)

def login_view(request):
	context = {}
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid() == False:
			form = LoginForm()

		else:
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			context = {
				"username": username,
				"password": password
			}

		if user is not None:
			login(request, user)
			return redirect("todolist:index")

		else:
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
			duplicates = ToDoItem.objects.filter(task_name=task_name)	

			if not duplicates:
				ToDoItem.objects.create(task_name=task_name, description=description, date_created=timezone.now(), user_id=request.user.id)
				return redirect("todolist:index")
			else:
				context = {
					"error": True
				}
	return render(request, "todolist/add_task.html", context)

def add_event(request):
	context = {}
	if request.method == 'POST':
		form = AddEventForm(request.POST)
		if form.is_valid() == False:
			form = AddEventForm()
		else:
			event_name = form.cleaned_data['event_name']
			description = form.cleaned_data['description']
			duplicates = Event.objects.filter(event_name=event_name)	
			if not duplicates:
				Event.objects.create(event_name=event_name, event_description=description, event_date=timezone.now(), user_id=request.user.id)
				return redirect("todolist:index")
			else:
				context = {
					"error": True
				}
	return render(request, "todolist/add_event.html", context)

def update_task(request, todoitem_id):
	todoitem = ToDoItem.objects.filter(pk=todoitem_id)
	context = {
		"user": request.user,
		"todoitem_id": todoitem_id,
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
