from django.urls import path
from . import views
urlpatterns = [

    path('donate_money/', views.donate_money_submit, name="donate_money_submit")
]
