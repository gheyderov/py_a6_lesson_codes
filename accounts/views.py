from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(False)
    context = {"form": form}
    return render(request, "register.html", context)


def login(request):
    form = LoginForm()
    if request.method == "POST":
        next = request.GET.get('next', reverse_lazy('home'))
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if not user:
                messages.add_message(request, messages.ERROR, "User not found!")
            else:
                django_login(request, user)
                return redirect(next)
    context = {"form": form}
    return render(request, "login.html", context)


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('login'))


@login_required(login_url='login')
def profile(request):
    return render(request, 'user-profile.html')