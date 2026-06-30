
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

def dashboard_page(request):
    return render(request, "dashboard.html")

urlpatterns = [



    # HTML Pages
    path("", home),
    path("login/", login_page),
    path("register/", register_page),
    path("dashboard/", dashboard_page),

    # REST APIs
    path("api/users/", include("users.urls")),

]