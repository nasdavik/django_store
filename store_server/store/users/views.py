from django.shortcuts import render

from users.models import User
from users.forms import UserLoginForm


def login(request):
    context = {
        'title': 'Авторизация',
        'form': UserLoginForm()
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'Регистрация'
    }
    return render(request, 'users/register.html', context)
