from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:groceryitem_id>/', views.groceryitem, name='viewgroceryitem'),
]