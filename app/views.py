from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 

def string1 (request):
    return HttpResponse('This is my first String response')

def string2 (request):
    return HttpResponse('This is a second String response')

def string3 (request):
    return HttpResponse('This is a third String response')