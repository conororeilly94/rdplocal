from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts
from main.models import Main
from django.core.files.storage import FileSystemStorage

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

        try: 

            myfile = request.FILES['myfile']
            fs = FileSystemStorage() # Make an object
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:


                    b = Posts(name = poststitle, short_txt = postsummary, body_txt = postbody, date = "2020", img = filename, imgurl = url, author = "-", 
                                catname = postscat, catid = 0, views = 0)
                    b.save()
                    return redirect('posts_list')

                else:

                    error = "Your File is Larger than 5 MB"
                    return render(request, 'back/error.html', {'error':error})
            
            else:

                # Come back to lecture 148
                error = "Your File is Not Supported"
                return render(request, 'back/error.html', {'error':error})

        except:

            error = "Please Input Your Content"
            return render(request, 'back/error.html', {'error':error})
    
    return render(request, 'back/posts_add.html')