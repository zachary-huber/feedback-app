from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('createsurvey/', views.createsurvey, name="createsurvey"),
    path('landingpage/', views.landingpage, name="landingpage"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('QRcode/', views.QRcode, name="QRcode"),
    path('signup/', views.signup, name="signup"),
    path('survey/', views.survey, name="survey"),
    path('thanks/', views.thanks, name="thanks"),
]