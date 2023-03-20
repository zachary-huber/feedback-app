from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('landingpage/', views.landingpage, name="landingpage"),
    
    path('survey/', views.survey, name="survey"),
    path('survey/<int:form_id>/', views.survey, name="survey"),
    path('thanks/', views.thanks, name="thanks"),
    path('formEditor/', views.formEditor, name="formEditor"),
    path('saveFormEditor/', views.saveFormEditor, name="saveFormEditor"),
    path('saveResponses/', views.saveResponses, name="saveResponses"),
    path('results/', views.results, name="results"),
    path('results/<int:form_id>/', views.results, name="results"),
    path('deleteForm/', views.deleteForm, name="deleteForm"),
]