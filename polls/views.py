from django.shortcuts import render

# matt, this is new, what they see on DB
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
