from django.shortcuts import render

#Importing Http Response
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("Hello Django")

def learn_python(request):
    return HttpResponse('<h1>Hello Python</h1>')
    