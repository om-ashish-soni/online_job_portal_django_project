from http.client import OK
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home), 
    path('hrhome',views.hrhome), 
    path('candidatehome',views.candidatehome), 
    path('confirmation',views.confirmation), 
    path('signin', views.signin),
    path('login', views.login),
    path('validateSignin', views.validateSignin),
    path('validateLogin', views.validateLogin),
    path('craftApplication', views.craftApplication),
    path('postApplication', views.postApplication),
    path('readApplication/<str:appid>/', views.readApplication),
    path('getMyApplications/<str:hremail>/',views.getMyApplications),
    path('searchJob',views.searchJob),
    path('searchJobApplication',views.searchJobApplication),
    path('applyApplication/<str:appid>/',views.applyApplication),
    path('addApplicant',views.addApplicant),
    path('appliedApplications/<str:candidateemail>/',views.appliedApplications),
    path('checkAppliedApp/<str:applicantid>/',views.checkAppliedApp),
    path('checkApplicants/<str:appid>/',views.checkApplicants),
    path('lookApplicant/<str:applicantid>/',views.lookApplicant),
    path('shortlistCandidate/<str:applicantid>/',views.shortlistCandidate),
    path('about/',views.about),
]