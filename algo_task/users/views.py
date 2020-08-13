from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate



def index(request):
	users = User.objects.all()
	context = {"users":users}

	if request.method == "POST":
		user_list = request.POST.getlist("user")
		obj = User.objects.filter(id__in=user_list)
		obj.delete()
	return render(request, 'index.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
	context = {"message":"",
				"is_login":True}
	if request.method == "GET":
		return render(request, 'login.html', context)
	if request.method == "POST":
		username = request.POST.get("email")
		password = request.POST.get("password")
		print (username, password)
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return redirect("home")
		else:
			context["is_login"] = False
			context["message"] = "Invalid username or password"
			return render(request, 'login.html', context)


def user_signup(request):
	context = {"message":"",
				"is_signup":True}
	if request.method == "GET":
		return render(request, 'signup.html', context)
	if request.method == "POST":
		username = request.POST.get("email")
		password = request.POST.get("password")
		name = request.POST.get("name")
		if User.objects.filter(username=username).exists():
			context["is_signup"] = False
			context["message"] = "User Already Exists."
			return render(request, 'signup.html', context)
		else:
			obj = User.objects.create(username=username, 
										email=username, 
										name=name)
			obj.set_password(password)
			obj.save()
			return redirect("login")
