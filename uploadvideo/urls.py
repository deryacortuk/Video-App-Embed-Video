from os import name
from django.urls import path
from . import views

app_name="video"

urlpatterns =[

path('dashboard/',views.dashboard,name="dashboard"),
path('add/',views.videoadd,name="addvideo"),
path('update/<int:id>',views.videoupdate,name="update"),
path('delete/<int:id>',views.deletevideo,name="delete"),
path('embed/',views.embedded,name="embed"),



]