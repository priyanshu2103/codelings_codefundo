from django.shortcuts import render,redirect

# Create your views here.
def main_page(request):
    return render(request,'home_page/main_page.html')
