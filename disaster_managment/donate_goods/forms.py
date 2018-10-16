from django.forms import ModelForm
from .models import donate_goods
from django import forms


class Goods(ModelForm):
    class Meta:
        model = donate_goods
        fields = '__all__'


class RawGoodsForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "your/organisations name here",}))
    Phone_Number = forms.CharField()
    Email = forms.EmailField()
    Vehicles_Numbers = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "enter all the vehicles numbers on a new line",
            "rows":10,
        }
    )
    )
    Water = forms.IntegerField(widget=forms.NumberInput)
    Packets_of_FoodItems = forms.IntegerField(widget=forms.NumberInput)
    Medicines = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "enter the name, use and quantity of each medicine",}))
    Date = forms.DateField(widget=forms.DateTimeInput(attrs={"placeholder":"date in yyyy-mm--dd",}))
