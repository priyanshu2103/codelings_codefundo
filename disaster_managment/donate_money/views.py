from django.shortcuts import render,redirect
from .forms import Money, RawMoneyForm
from .models import donate_money
# Create your views here.


def donate_money_submit(request):
    if request.method == "POST":
        form = RawMoneyForm(request.POST)
        if form.is_valid():
            # form_item = form.save(commit=False)
            # form_item.save()
            donate_money.objects.create(**form.cleaned_data)
            #return redirect("information added successfully")
    else:
        form = RawMoneyForm()
    return render(request, 'donate_money/donate_money_index.html', {'form': form})
