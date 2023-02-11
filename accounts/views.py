from django.shortcuts import render

# Create your views here.


from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    print('step 1 is working ---------------------')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        print('step 2 is working ---------------------')
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html', {'error': 'Username already exists'})
        except User.DoesNotExist:
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'register.html')

def logout(request):
    auth_logout(request)
    return redirect('/')