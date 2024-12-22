from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Post


def index(request):
    return render(request, "network/index.html", {
        "posts": Post.objects.all().order_by('-id')
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required(login_url='/login')
def post(request):
    if request.method == "POST":
        post_content = request.POST.get("post", "").strip()

        if not post_content:
            return render(request, "network/index.html", {
                "message": "Post content cannot be empty."
            })

        try:
            Post.objects.create(
                post=post_content,
                user=request.user
            )
        except Exception as e:
            return render(request, "network/index.html", {
                "message": f"An error occurred: {str(e)}"
            })

        return HttpResponseRedirect(reverse("index"))

    return render(request, "index.html")


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, "network/profile.html", {
        "user_profile_name": user,
        "posts": Post.objects.filter(user=user).order_by('-id')
    })
