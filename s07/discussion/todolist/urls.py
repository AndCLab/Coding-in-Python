from django.urls import path
from . import views

# Syntax:
# path(route, view, name)

urlpatterns = [
	path('', views.index, name='index'),

]