from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        username= request.POST["username"]
        password= request.POST["password"]
        try:
            user = User.objects.get(username=username)
            return render(request,'survey/home_page.html',{"error":"Username already Taken"})
        except User.DoesNotExist:
            user = User.objects.create_user(username=username,password=password)
            auth.login(request, user)
            return render(request,'survey/create_survey_page.html')
    # return render(request, 'signup.html')

def login(request):
    # return render(request, 'signup.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home_page')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home_page')
    # html = "<html><body>Logout Page</body></html>"
    # return HttpResponse(html)