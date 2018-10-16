from django.urls import path
from . import views
urlpatterns = [

    path('donate_goods/donate_goods_submit', views.donate_goods_submit, name="donate_goods_submit")
]