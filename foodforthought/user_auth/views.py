from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterUserForm

# Create your views here.
def index(request):
    '''Landing page for login/registration'''
    return render(request, 'authentication/index.html')


def user_login(request):
    '''View for user login'''
    return render(request, 'authentication/login.html')


def show_user(request):
    '''Method to show authenticated user.'''
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def authenticate_user(request):
    '''Method to authenticate user.'''
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
            )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('polls:home')
        )
    

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("polls:home")
    else:
        form = RegisterUserForm()    
    return render(request, 'authentication/register.html', { "form": form })

