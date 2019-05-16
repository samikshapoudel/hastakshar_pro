from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'AppOne/index.html')


def login(request):
    return render(request, 'AppOne/login.html')

def signup(request):
    return render(request, 'AppOne/signup.html')