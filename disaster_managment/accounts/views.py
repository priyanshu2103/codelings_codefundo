from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from .forms import UserLoginForm, VolunteerRegisterProfilerForm
from .forms import CustomUserCreationForm,UserLoginForm
from .models import Volunteer
from django.contrib import messages
from django.forms import BaseModelForm
#from .models import Volunteer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm




# def register_as_volunteer_view(request):
#     title = "Register as Volunteer"
#
#     UserForm = VolunteerRegisterUserForm(request.POST or None)
#     ProfileForm = VolunteerRegisterProfilerForm(request.POST or None)
#
#     if UserForm.is_valid() and ProfileForm.is_valid():
#         user = UserForm.save(commit=False)
#
#         # ProfileForm.save()
#         password = UserForm.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#
#
#     else:
#         messages.error(request, 'Please correct the errors below')
#     # else:
#     #     userform = VolunteerRegisterUserForm(instance=request.user)
#     #     profileform = VolunteerRegisterProfilerForm(instance=request.user)
#
#     return render(request, 'accounts/register.html', context={'UserForm': UserForm, 'ProfileForm': ProfileForm, 'title': title})

def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        #redirect
    return render(request, 'accounts/login.html', context={"form": form, "title": title})


def logout_view(request):
    logout(request)
    return render(request, 'accounts/login.html', context={})


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': f})


def register_as_group_view(request):
    return render(request, '', context={})


def register_as_volunteer(request):
    #ProfileForm = VolunteerRegisterProfilerForm(request.POST or None)
    if request.method == "POST":
        form1 = VolunteerRegisterProfilerForm(request.POST)
        if form1.is_valid():
            Volunteer.objects.create(**form1.cleaned_data)
    else:
        form1 = VolunteerRegisterProfilerForm()
    return render(request, 'accounts/register_as_volunteer.html', {'form1': form1})
