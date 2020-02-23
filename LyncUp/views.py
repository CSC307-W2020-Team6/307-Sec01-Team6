from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

# posts = [
#     {
#         'author': 'GabyDaddy',
#         'title': 'Boof',
#         'content': 'Now thats what I call Content!',
#         'date_posted': 'April 20, 2020'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, "LyncUp/home.html", context)

def about(request):
    return render(request, "LyncUp/about.html", {'title' : 'About'})
