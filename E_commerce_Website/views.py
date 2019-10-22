from django.shortcuts import render

# Create your views here.

def HomePage(request):

      return render(request, "E_commerce_Website/home.html")
