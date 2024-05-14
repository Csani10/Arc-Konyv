from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from . import models
import hashlib

# Create your views here.
def index(request):
    if "register" in request.GET:
        #us = models.User()
        #us.email = request.GET.get("email")
        #us.username = request.GET.get("username")
        #us.password = hashlib.sha256(request.GET.get("password").encode("utf-8")).hexdigest()
        #print(us.password)
        #us.save()
        user = User.objects.create_user(request.GET.get("username"), request.GET.get("email"), request.GET.get("password"))
        user.save()
    elif "login" in request.GET:
        user = auth.authenticate(request, username=request.GET.get("username"), password=request.GET.get("password"))
        if user is not None:
            auth.login(request, user)
            print("igen")
            return redirect("user/")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("/")


    return render(request, "index.html")

def user(request):
    if "logout" in request.GET:
        auth.logout(request)
    usr = auth.get_user(request)
    print(usr.username)
    print(usr.is_anonymous)
    if usr.is_anonymous:
        return redirect("/")
    return render(request, "user.html", {"neve": usr.username})

def test(request):
    return render(request, "base.html")