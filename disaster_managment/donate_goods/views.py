from django.shortcuts import render,redirect
from .forms import Goods, RawGoodsForm
from .models import donate_goods
# Create your views here.


def donate_goods_submit(request):
    if request.method == "POST":
        form = RawGoodsForm(request.POST)
        if form.is_valid():
            # form_item = form.save(commit=False)
            # form_item.save()
            donate_goods.objects.create(**form.cleaned_data)
            #return redirect("information added successfully")
    else:
        form = RawGoodsForm()
    return render(request, 'donate_goods/donate_goods.html', {'form': form})
