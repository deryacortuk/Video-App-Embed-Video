from django.urls import path
from . import views

app_name= "user"

urlpatterns = [   
  path('register/',views.signupuser,name="register"),
  path('login/',views.signinuser,name="login"),
  path('logout/',views.logout_user,name="logout"),
  
]
