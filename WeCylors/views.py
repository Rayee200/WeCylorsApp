from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Homepage Test</h1><div><a href='./blog'>Module blog</a></div><br><div><a href='./admin'>Behind</a></div>")