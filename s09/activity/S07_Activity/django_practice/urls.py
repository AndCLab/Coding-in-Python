from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:groceryitem_id>/', views.groceryitem, name='viewgroceryitem'),
	path('register', views.register, name='register'),
	path('change_password', views.change_password, name='change_password'),
	path('login', views.login_view, name='login'),
	path('logout', views.logout_view, name='logout'),
]