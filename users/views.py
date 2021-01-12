from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def user(request):
#     return HttpResponse('User Home')

def register(request):
    return HttpResponse('<h1>users register Page</h1>')

def login(request):
    return HttpResponse('<h1>users Login Page</h1>')
