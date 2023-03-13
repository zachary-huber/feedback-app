from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.urls import path
from .models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # projects = Project.objects.all()
    # context = { 'projects':projects}
    return render(request, 'projects/Home.html')

@login_required(login_url='login')
def createsurvey(request):
    return render(request, 'projects/CreateSurvey.html')

@login_required(login_url='login')
def landingpage(request):
    return render(request, 'projects/LandingPage.html')

def login(request):
    return render(request, 'projects/Login.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'projects/Profile.html')

def QRcode(request):
    return render(request, 'projects/QRcode.html')

def signup(request):
    return render(request, 'projects/Signup.html')

def survey(request):
    return render(request, 'projects/Survey.html')

def thanks(request):
    return render(request, 'projects/Thanks.html')


@login_required
def formEditor(request):
    return render(request, 'projects/formEditor.html')
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