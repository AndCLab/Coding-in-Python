from django.urls import path
from . import views

# Syntax: path(route, view, name)

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todoitem_id>/', views.todoitem, name='todoitem'),
    path('register', views.register, name='register'),
    path('change_password', views.change_password, name='change_password'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
]
