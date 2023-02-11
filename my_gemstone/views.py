from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def index(request):
    
    return render(request, 'index.html')
