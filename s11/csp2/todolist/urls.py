from django.urls import path
from . import views

# Syntax: path(route, view, name)

app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todoitem_id>/', views.todoitem, name='todoitem'),
    path('<int:eventitem_id>/eventitem/', views.eventitem, name='eventitem'),
    path('register', views.register, name='register'),
    path('change_password', views.change_password, name='change_password'),
    path('update_profile/<int:user_id>', views.update_profile, name='update_profile'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('add_task', views.add_task, name="add_task"),
    path('add_event', views.add_event, name="add_event"),
    path('<int:todoitem_id>/edit', views.update_task, name='update_task'),
    path('<int:todoitem_id>/delete', views.delete_task, name='delete_task'),
]
