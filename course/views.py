

#Importing Http Response
from django.http import HttpResponse
from django.shortcuts import render

# def learndjango(request):
#     return HttpResponse("Hello Django")

# def learnpython(request):
#     return HttpResponse('<h1>Hello Python</h1>')

def course(request):
    return render(request,'course/course.html')
