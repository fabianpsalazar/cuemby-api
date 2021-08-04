from django.conf.urls import url
from django.urls import path 
from fifa import views

urlpatterns = [
    path('fifa', views.Fifa_api.as_view()),
]
