from django.shortcuts import render
from django.http import HttpResponse
# create your view here 
def index(request):

    return HttpResponse("Hello world from application")