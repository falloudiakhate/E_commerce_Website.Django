from django.urls import path
from Accounts import views

urlpatterns = [

    path('Login', views.Login, name = "Login"),

    path('Signup', views.Signup, name = "Signup"),

     path('Logout', views.Logout, name = "Logout"),

]
