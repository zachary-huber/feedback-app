from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.urls import path
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

from projects.models import Forms

# Create your views here.

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html') #########
    
def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('profiles')
        
        else:
            messages.error(request, 'An error has occurred!')


    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)


def user_forms(request, idd):
    # Retrieve the user object based on the user_id
    user_id = User.objects.get(id=idd)

    # Retrieve all forms associated with the user
    user_forms = Forms.objects.filter(user_id=idd)

    form_ids = []
    form_titles = []
    for user_form in user_forms:
        form_ids.append(user_form.form_id)
        form_titles.append(user_form.title)
        
    forms = zip(form_ids, form_titles)
    print(forms)
    # get form title from user_forms
    
    # passing the user_id, user_forms, form_ids, and form_titles to the profiles.html template
    return render(request, 'users/profiles.html',  {'id': user_id, 'forms': forms})


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    user_id = request.user.id
    return user_forms(request, user_id)
    
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile':profile}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request, 'users/account.html', context)

