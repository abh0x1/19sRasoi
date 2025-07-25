from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'core/home.html')

def login(req):
    return render(req,'core/login.html')

def signup(req):
    return render(req,'core/signup.html')

def about(req):
    return render(req,'core/about.html')