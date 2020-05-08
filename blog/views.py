from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    latest_list = Post.objects.order_by('-publish')
    output = '\n'.join([q.title for q in latest_list])
    return HttpResponse(output)
