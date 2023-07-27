from django.urls import path
from . import views

# Syntax: path(route, view, name)

app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todoitem_id>/', views.todoitem, name='todoitem'),
    path('register', views.register, name='register'),
    path('change_password', views.change_password, name='change_password'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('add_task', views.add_task, name="add_task"),
    path('<int:todoitem_id>/edit', views.update_task, name='update_task'),
    path('<int:todoitem_id>/delete', views.delete_task, name='delete_task'),
]
