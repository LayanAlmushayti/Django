from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')  # ❌ Fail
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'You have successfully registered.')  # ✅ Success
        return redirect('login')

    return render(request, 'usermodule/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')  # ✅
            return redirect('books.index')
        else:
            messages.error(request, 'Invalid username or password.')  # ❌
    return render(request, 'usermodule/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')  # 👋
    return redirect('login')

