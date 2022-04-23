from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_todos, name='list_todos'),
    path('create/', views.create_todo, name='create_todo'),    
    path('update/<id>/', views.update_todo,name='update_todo'),
    path('delete/<id>/', views.delete_todo, name='delete_todo'),
    path('<id>/', views.todo_detail, name='todo_detail'),
]
