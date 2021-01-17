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


def posts_add(request):
    

    if request.method == 'POST':

        poststitle = request.POST.get('poststitle')
        postscat = request.POST.get('postscat')
        postsummary = request.POST.get('postsummary')
        postbody = request.POST.get('postbody')

        if poststitle == '' or postsummary == '' or postbody == '' or postscat == '':
            error = "All Fields are Required"
            return render(request, 'back/error.html', {'error':error})

        
        b = Posts(name = poststitle, short_txt = postsummary, body_txt = postbody, date = "20202", img = "-", author = "-", 
                    catname = postscat, catid = 0, views = 0)
        b.save()
        return redirect('posts_list')
    
    return render(request, 'back/posts_add.html')