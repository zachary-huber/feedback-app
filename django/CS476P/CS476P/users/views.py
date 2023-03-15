from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.urls import path
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

import json
from django.http import JsonResponse
from .models import Forms
from django.contrib import messages



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


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
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


@login_required
def formEditor(request):
    return render(request, 'users/formEditor.html')
    # if request.method == 'POST':
        
    #     my_variable = request.POST.get('myVariable', None)
    #     user_id = request.user.id
    #     try:
    #         json_data = json.loads(my_variable)
    #     except ValueError:
    #         return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    #     form = Form(user_id=user_id, json_data=json_data)
    #     form.save()
    #     return JsonResponse({'status': 'ok'})
    #     return HttpResponse('Form submitted')
    # else:
    #     render(request, 'projects/formEditor.html')
    #     return HttpResponse('Form submitted')
    
    
@login_required
def saveFormEditor(request):   
    # return render(request, 'projects/saveFormEditor.html')
    if request.user.is_authenticated:
        if request.method == 'POST':
            json_data = request.body.decode('utf-8')  # decode the request body
            user_id = request.user.id
            
            # get the form title from the JSON data
            newFormTitle = list(json.loads(json_data)[0].values())[0]
            
            form = Forms(form_json=json_data, user_id=user_id, title=newFormTitle)  # create a Form object with the JSON data
            form.save()  # save the Form object to the database
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    else:
        return JsonResponse({'status': 'error', 'message': 'User is not authenticated'})
