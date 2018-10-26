from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from .models import Volunteer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


User = get_user_model()
GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)


#for login
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("user not registered")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(UserLoginForm, self).clean()


# class VolunteerRegisterUserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput, label="set your profile password")
#     password2 = forms.CharField(widget=forms.PasswordInput, label="confirm password", required=True)
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username', 'password', 'password2']
#
#     def clean_password2(self):
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#         if password != password2:
#             raise forms.ValidationError("Passwords must match.")
#         return password
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
#             raise forms.ValidationError(u'Username "%s" is already in use.' % username)
#         return username


class VolunteerRegisterProfilerForm(forms.Form):
    username = forms.CharField()
    Age = forms.IntegerField(widget=forms.NumberInput)
    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    Locality = forms.CharField(widget=forms.Textarea)
    City = forms.CharField()
    State = forms.CharField()
    Pin = forms.IntegerField(widget=forms.NumberInput)
    PhoneNumber = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Volunteer
        fields = '__all__'




class CustomUserCreationForm(forms.Form):
    first_name = forms.CharField(label='Enter first name', max_length=50)
    last_name = forms.CharField(label='Enter last name', max_length=50)
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            email = self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        return user
