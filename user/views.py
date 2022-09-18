from django.http import HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.utils.html import escape

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from user.queries import *

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def user_login(request):
    if request.method == "POST":
        email = escape(request.POST.get('email'))
        password = escape(request.POST.get('password'))
        user = authenticate(request, email=email, password=password)
        if user is None:
            messages.add_message(request, messages.INFO, 'Login Failed!')
            return redirect("login_view")
        
        else:
            # print(user)
            login(request, user)
            return redirect("homepage")

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def user_signup(request):
    if request.method == "POST":
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if is_exist(email):
            messages.add_message(request, messages.INFO, 'Email already exist! Try with different Email')
            return redirect("signup_view")
        else:
            if(password.strip() == password1.strip()):
                try:
                    create_user(fname, lname, email, password)
                    messages.add_message(request, messages.INFO, 'Your account has been created sucessfully!')
                    return redirect("login_view")
                
                except:
                    if(email == ""):
                        messages.add_message(request, messages.INFO, 'Email Required!')
                    else:
                        messages.add_message(request, messages.INFO, 'Error in Sign up!')
                    return redirect("signup_view")
            else:
                messages.add_message(request, messages.INFO, 'Confirm Password is not same!')
                return redirect("signup_view")


    else:
        return HttpResponseBadRequest("<h1>Bad Request</h1>")


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logged Out')
    return redirect("login_view")


# def show_profile(request):
#     user = UserSerializer(request.user)
#     data = user.data
#     data["logged_in"] = not (request.user.is_anonymous)
#     return render(request, 'profile.html', data)