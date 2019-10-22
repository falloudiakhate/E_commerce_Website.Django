from django.shortcuts import render, redirect, reverse

from django.contrib.auth.forms import UserCreationForm

from Accounts.forms import UserForm, LoginForm

from django.contrib.auth import authenticate, login, logout




def Signup(request):

      if request.method == "POST":

            form = UserForm(request.POST)

            if form.is_valid():

                  form.save()
                  return redirect("Login")

            form = UserForm()
            return render(request, "Accounts/signup.html" ,{"form":form})

      form = UserForm()
      return render(request, "Accounts/signup.html" ,{"form":form})



def Login(request):

      if request.method == "POST":

            form = LoginForm(request.POST)

            if form.is_valid():

                  username = form.cleaned_data.get("username")
                  password = form.cleaned_data.get("password")

                  user = authenticate(username = username, password = password)

                  if user:

                        login(request, user)
                        return redirect("HomePage")

                  else:

                        form = LoginForm()
                        return render(request, "Accounts/login.html", {"form" : form})

      form = LoginForm()
      return render(request, "Accounts/login.html", {"form" : form})



def Logout(request):

      logout(request)
      return redirect(reverse(Login))

