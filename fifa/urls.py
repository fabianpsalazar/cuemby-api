from django.conf.urls import url
from django.urls import path 
from fifa import views

urlpatterns = [
    # for GET
    path('v1/players', views.Fifa_api.as_view({'get':'get'})),
    # for POST
    path('v1/teams',views.Fifa_api.as_view({'post':'get'}))
]
