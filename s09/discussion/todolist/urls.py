from django.urls import path
from . import views

# Syntax:
# path(route, view, name)

urlpatterns = [
	path('', views.index, name='index'),
	#path('<int:todoitem_id>/', views.todoitem, name='viewtodoitem'),
	path('register', views.register, name='register')
]

