from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.
@login_required
def home(request):
    tasks = Task.objects.all()
    return render(request,"todo/index.html",{"tasks": tasks})
@login_required
def add_task(request):
    title = request.POST.get("title")
    description = request.POST.get("description")
    if request.method == "POST":
        tasks = Task.objects.create(Title=title,Description=description,Is_Done=False)
    return redirect("/todo")
@login_required
def remove_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/todo")
@login_required
def update_task_status(request,id):
    task = Task.objects.get(id=id)
    task.Is_Done = not task.Is_Done
    task.save()
    return redirect("/todo")
def signup_page(request):
    if request.method == "POST":
        first_name = request.POST.get("First-Name")
        last_name = request.POST.get("Last-Name")
        email = request.POST.get("Email")
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        if User.objects.filter(username=username).exists():
            print("User already exists")
        else:
            if User.objects.filter(email=email).exists():
                print("A different user already uses that email")
            else:
                user = User.objects.create_user(username,email,password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                login(request,user=user)
                return redirect("/todo")
                

    return render(request,"todo/signup.html")
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user=user)
            return redirect('/todo')
            print("Auth")
        else:
            print("NotAuth")

    return render(request,'todo/login.html')
def logout_page(request):
    logout(request)
    return redirect('/todo')
