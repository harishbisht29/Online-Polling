from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        username= request.POST["username"]
        password= request.POST["password"]
        try:
            user = User.objects.get(username=username)
            return render(request,'survey/home_page.html',{"error":"Username already Taken"})
        except User.DoesNotExist:
            user = User.objects.create_user(username, password)
            auth.login(request, user)
            return redirect('home_page')
    # return render(request, 'signup.html')

def login(request):
    return render(request, 'signup.html')

def logout(request):
    return render(request, 'signup.html')