from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="TodoAppHome"),
    path('add_task/', views.add_task,name="TodoAppAddTask"),
    path('rm_task/<id>',views.remove_task,name="TodoAppRemoveTask"),
    path('update_task_status/<id>',views.update_task_status,name="TodoAppUpdateTaskStatus")

]