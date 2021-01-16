from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts
from main.models import Main

# Create your views here.

def posts_detail(request, word):
    
    site = Main.objects.get(pk=2)
    posts = Posts.objects.filter(name=word)

    return render(request, 'front/posts_detail.html', {'posts':posts, 'site':site})


def posts_list(request):

    posts = Posts.objects.all()
    
    return render(request, 'back/posts_list.html', {'posts':posts})