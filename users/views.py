from django.contrib.auth.models import User
from imaplib import IMAP4
from django.shortcuts import render
from django.contrib.auth import login, logout

def authenticate(username=None, password=None):
    try:
        # Check if this user is valid on the mail server
        c = IMAP4('newmailhost.cc.iitk.ac.in')
        c.login(username, password)
    except:
        return None

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # Create a new user. There's no need to set a password
        # because only the password from settings.py is checked.
        user = User(username=username)
        user.save()

    return user

def login_user(request):
    #if user is already logged in, return them to homepage
    if request.user.is_authenticated:
        return render(request, 'users/index.html', {'error_message': 'You are already logged in!'})
    #process form data
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username=username, password=password)
        #if user exists
        if user is not None:
            login(request, user)
            return render(request, 'users/index.html')
        else:
            return render(request, 'users/login.html', {'error_message': 'Invalid login'})
    return render(request, 'users/login.html')

def logout(request):
    logout(request)
    return render(request, 'users/login.html', {"form": form})
