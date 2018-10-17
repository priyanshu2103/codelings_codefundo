from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout,get_user_model
from .forms import UserLoginForm


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request, user)
        #redirect
    return render(request, 'accounts/login.html', context={"form": form, "title": title})


def register_as_volunteer_view(request):
    return render(request,'',context={})


def register_as_group_view(request):
    return render(request, '', context={})


def logout_view(request):
    logout(request)
    return render(request, 'accounts/login.html', context={})
