from django.shortcuts import render, HttpResponse

def Homepage(request):
    return HttpResponse('Hello, world!')

def Contacts(request):
    return HttpResponse('Contacts')

def About_Us(request):
    return HttpResponse('About_Us')

# Create your views here.
