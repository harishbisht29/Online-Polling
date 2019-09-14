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
            user = User.objects.create_user(username, password)
            auth.login(request, user)
            return redirect('home_page')
    # return render(request, 'signup.html')

def login(request):
    # return render(request, 'signup.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        html = "<html><body>Login Page"+username+" " + password +"</body></html>"
        return HttpResponse(html)

def logout(request):
    return render(request, 'signup.html')
    html = "<html><body>Logout Page</body></html>"
    return HttpResponse(html)