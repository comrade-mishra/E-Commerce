from django.shortcuts import render, redirect
from .forms import registeration_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'user_example/index.html')


def Register(request):

    if request.user.is_authenticated:
        return redirect('index')

    else:
        form = registeration_form()
        if request.method == 'POST':
            form = registeration_form(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}

        return render(request, 'registration/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username = username, password = password)

            if user is not None:

                login(request, user)
                return redirect('index')
            
            else:
                
                messages.info(request, 'Username OR password is incorrect')
                
        
        context = {}

        return redirect('registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')