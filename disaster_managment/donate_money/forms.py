from django.forms import ModelForm
from .models import donate_money
from django import forms


class Money(ModelForm):
    class Meta:
        model = donate_money
        fields = '__all__'


class RawMoneyForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "your/organisation name here"}))
    Phone_Number = forms.CharField()
    Email = forms.EmailField()
    Amount = forms.IntegerField()
