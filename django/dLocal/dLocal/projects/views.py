from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.urls import path
from .models import Project
from django.contrib.auth.decorators import login_required

import json
from django.http import JsonResponse
from .models import Forms
from django.contrib import messages

from users.models import User
from projects.models import Forms
from projects.models import Responses

import pandas as pd

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


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

def survey(request, form_id):
    form = Forms.objects.get(form_id=form_id)
    form_JSON = form.form_json
    return render(request, 'projects/Survey.html', {'form_id': form_id, 'form_JSON': form_JSON})

def thanks(request):
    return render(request, 'projects/Thanks.html')


@login_required(login_url='login')
def formEditor(request):
    if not (request.user.is_authenticated):
        return redirect('https://commentcorner.ngrok.app/users/login/')
    else:
        return render(request, 'projects/formEditor.html')
    
    
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


@login_required
def deleteForm(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            json_data = request.body.decode('utf-8')  # decode the request body
            formID = json.loads(json_data)
            
            form = Forms.objects.get(form_id=formID)
            form.delete()
            
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
        
    return HttpResponseRedirect(reverse('index'))


def saveResponses(request):   
    # return render(request, 'projects/saveFormEditor.html')
    # if request.user.is_authenticated:
    if request.method == 'POST':
        json_data = request.body.decode('utf-8')  # decode the request body
        # user_id = request.user.id
        
        json_data = list(json.loads(json_data).values())
        
        responseDate = json_data[0]
        responseFormID = json_data[1]
        responseJSON = json_data[2]
        
        # print the 3 vars above
        print(responseJSON)
        print(responseDate)
        print(responseFormID)
        
        response = Responses(response_json=responseJSON, created_at=responseDate, form_id=responseFormID)  # create a Form object with the JSON data
        response.save()  # save the Form object to the database
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    

@login_required
def results(request, form_id):
    if request.user.is_authenticated:
        current_user = request.user.id
        
        form = Forms.objects.get(form_id=form_id)
        if form.user_id != current_user:
            messages.error(request, 'You do not have permission to view this page')
            return redirect('home')
        
        results = Responses.objects.filter(form_id=form_id)
        
        # Create a list of all the response JSONs
        newList = []
        for responseObject in results:
            response_list = json.loads(responseObject.response_json)
            for list in response_list:
                newList.append(list)
            
        # Create a dictionary of unique responseHeadings and values
        response_dict = {}
        for item in newList:
            heading = item['responseHeading']
            value = item['responseValue']
            if isinstance(value, str):
                value = item['responseValue'].strip()
            
            if heading not in response_dict:
                response_dict[heading] = [value]
            else: # value not in response_dict[heading]:
                response_dict[heading].append(value)
        
        # convert a dictionary into a dataframe
        df = pd.DataFrame(response_dict)
        df =  df.reset_index(drop=True)
        results_table = df.to_html(index=False)
    
        # return render(request, 'survey.html', {'form': form})
        return render(request, 'projects/results.html', {'form_id': form_id, 'results_table': results_table})
    else:   
        return JsonResponse({'status': 'error', 'message': 'User is not authenticated'})

def thanks(request):
    return render(request, 'projects/Thanks.html')