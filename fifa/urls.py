from django.conf.urls import url
from django.urls import path 
from fifa import views

urlpatterns = [
    # for GET
    path('v1/players', views.Fifa_get.as_view()),
    # for POST
    path('v1/teams', views.Fifa_post.as_view())
]
