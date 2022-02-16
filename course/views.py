from django.shortcuts import render

#Importing Http Response
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("Hello Django")