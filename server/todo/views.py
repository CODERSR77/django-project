from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request,"todo/index.html",{"tasks": tasks})
def add_task(request):
    title = request.POST.get("title")
    description = request.POST.get("description")
    if request.method == "POST":

        tasks = Task.objects.create(Title=title,Description=description,Is_Done=False)
    return redirect("/todo")
def remove_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/todo")