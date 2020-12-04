from bottle import HTTPResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.urls import reverse

from account.forms import RegisterForm, LoginForm


def sign(request):
    if request.method == "GET":
        return render(request, 'sign.html', {"error": ""})
    else:
        if "register" in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
        elif "login" in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                user = User.objects.filter(email=form.cleaned_data["email"]).first()
                if user:
                    valid = user.check_password(form.cleaned_data["password"])
                else:
                    valid = False
                if valid:
                    login(request, user)
                    return HttpResponseRedirect(reverse("home"))
            return render(request, 'sign.html', {"error": "ایمیل یا پسورد اشتباه می باشد."})

    return HTTPResponse()


@login_required(login_url="sign")
def home(request):
    return render(request, 'home.html', {})


def send_email(request):
    if request.method == "POST":
        pass
