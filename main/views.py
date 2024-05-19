from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from . import models
import hashlib

# Create your views here.
def index(request):
    if "register" in request.GET:
        return redirect("register/")
    elif "login" in request.GET:
        return redirect("login/")

    return render(request, "index.html")

def login(request):
    if "login" in request.GET:
        usr = auth.authenticate(username=request.GET.get("username"), password=request.GET.get("password"))
        if usr is not None:
            auth.login(request, usr)
            return redirect("/user/")
        else:
            messages.error(request, "Hibás felhasználónév vagy jelszó!")
    
    return render(request, "login.html")

def register(request):
    if "register" in request.GET:
        user = User.objects.create_user(request.GET.get("username"), request.GET.get("email"), request.GET.get("password"))
        user.first_name = request.GET.get("first_name")
        user.last_name = request.GET.get("last_name")
        user.save()
        if user:
            auth.login(request, user)
            return redirect("/user/")
    
    return render(request, "register.html")

def user(request):
    if "delete" in request.GET:
        post = models.Posts.objects.get(post=request.GET.get("text"), id=request.GET.get("id"))
        post.delete()
        return redirect("/user/")
    
    if "logout" in request.GET:
        auth.logout(request)
        return redirect("/")
    
    if "postbtn" in request.GET:
        usr = auth.get_user(request)
        post = models.Posts(username=usr.username, post=request.GET.get("post"))
        post.save()
        return redirect("/user/")

    usr = None
    user = None
    localuser = False
    if "id" in request.GET:
        user = User.objects.get(id=request.GET.get("id"))
    else:
        usr = auth.get_user(request)
        try:
            user = User.objects.get_by_natural_key(usr.username)
        except:
            pass
        print(usr.username)
        print(usr.is_anonymous)
        print(usr.id)
        localuser = True
        if usr.is_anonymous:
            return redirect("/")
    
    posts = models.Posts.objects.filter(
        username=user.username
    ).reverse()
    return render(request, "user.html", {"full_name": user.first_name + " " + user.last_name, "user_name": user.username, "is_local": localuser, "posts": posts})

def test(request):
    return render(request, "base.html")