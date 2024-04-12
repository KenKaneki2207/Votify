from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def votingUser(request):
    return HttpResponse("This is my Voting User Page")

def login_page(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if (User.objects.filter(username=username).exists() == True):
        message = "Username already taken"
    
    elif (password1 == password2) and (password1 != ''):
        user = User.objects.create_user(username, email, password1)
        user.save()
        return redirect('login')
    
    elif (password1!= password2):
        message = "Password didn't match"

    elif (password1 == '') and (password1 == password2):
        message = "Passwords can't be empty"
        
    return render(request, 'signup.html', {'message':message})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print('*************************',user,'**************************')
        if user is not None:
            login(request,user)
            print('************Successfully Login******************')
            return redirect('voting')
        message = 'Invalid Credentials'
    return render(request,'login.html', {'message':message}) 

def logout_user(request):
    logout(request)
    return render(request, 'home.html')
