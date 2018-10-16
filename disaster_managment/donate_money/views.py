from django.shortcuts import render
from .forms import Money
# Create your views here.


def donate_money_submit(request):
    if request.method == "POST":
        form = Money(request.POST)
        if form.is_valid():
            form_item = form.save(commit=False)
            form_item.save()
    else:
        form = Money()
    return render(request, 'donate_money/donate_money_index.html', {'form': form})
