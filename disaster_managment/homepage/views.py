from django.shortcuts import render,redirect

# Create your views here.



def main_page(request):
    return render(request, 'homepage/main_page.html')



