<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
=======
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def contact(request):
>>>>>>> f2e683044aaafdb905a72a34bad0582a9ae5a7ed
    return render(request, 'contact.html')