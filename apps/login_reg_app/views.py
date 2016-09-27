from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.core.exceptions import ValidationError
from .models import User
import bcrypt

def index(request):
    rform = RegisterForm()
    lform = LoginForm()
    context = {
        'registerform' : rform,
        'loginform' : lform
    }
    print User.objects.all()
    return render(request, 'login_reg_app/index.html', context)

def register(request):
    rform = RegisterForm()
    lform = LoginForm()

    if request.method == 'POST':
        doneform = RegisterForm(request.POST)
        doneform.is_valid()
        try:
            doneform.clean_password2()
            newpass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], feet=request.POST['feet'], inches=request.POST['inches'], weight=request.POST['weight'], age=request.POST['age'], password=newpass)
            request.session['user']=request.POST['email']
            context = {
                'user' : User.objects.all()
            }
            return render(request, 'login_reg_app/index.html', context)
        except ValidationError:
            context = {
                'registerform' : rform,
                'loginform' : lform,
                'errors' : doneform.errors
            }
            return render(request, 'login_reg_app/index.html', context)

def login(request):
    fform = LoginForm()

    if request.method == 'POST':
        doneform = LoginForm(request.POST)
        doneform.is_valid()
        try:
            doneform.checkMatch()
            request.session['user']=request.POST['email']
            context = {
                'users' : User.objects.all()
            }
            return render(request, 'login_reg_app/index.html', context)
        except ValidationError:
            context = {
                'registerform' : rform,
                'loginform' : lform,
                'errors' : doneform.errors
            }
            return render(request, 'login_reg_app/index.html', doneform.errors)