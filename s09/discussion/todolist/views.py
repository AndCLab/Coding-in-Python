from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
	return HttpResponse("Hello from the views.py file")

def register(request):
	users = User.objects.all()
	is_user_registered = False
	context = {
		"is_user_register": ise_user_registered
	}
	for indiv_user in users:
		if indiv_user.username == "johndoe":
			is_user_registered == True 
			break

	if is_user_register == False:
		user = User()
		user.username = "johndoe"
		user.first_name = "John"
		user.last_name = "Doe"
		user.email = "john@mail.com"
		#user.password = "john1234"
		user.set_password("john1234")
		user.is_staff = False
		user.is_active = store_trueuser.save()
		context= {
			"first_name": user.first_name,
			"last_name": user.last_name		
	}

	return render(request, "todolist/register.html", context)