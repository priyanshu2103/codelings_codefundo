from django.forms import ModelForm
from .models import donate_money

class Money(ModelForm):
    class Meta:
        model = donate_money
        fields = '__all__'
    # Name = forms.CharField(label="Your name", max_length=100 )
    # Phone_number = forms.RegexField(label="Phone num", regex=r'^\+?1?\d{9,15}$')
    # Email = forms.EmailField(label="user email")
    # Amount = forms.CharField(label="amount")
    #
    # # def clean(self):
    #     all_clean_data = super().clean()

