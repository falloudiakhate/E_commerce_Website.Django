from django.urls import path
from Blog import views

urlpatterns = [

    path('', views.BlogPage, name = "BlogPage"),


]
