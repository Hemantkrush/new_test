from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.


def homepage(request):
    return render(request, "homepage.html")

def login(request):
    return HttpResponse("logged in")



