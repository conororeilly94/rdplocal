from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcategory.models import SubCategory

# Create your views here.

def posts_detail(request, word):
    
    site = Main.objects.get(pk=2)
    posts = Posts.objects.filter(name=word)

    return render(request, 'front/posts_detail.html', {'posts':posts, 'site':site})


def posts_list(request):

    posts = Posts.objects.all()
    
    return render(request, 'back/posts_list.html', {'posts':posts})


def posts_add(request):

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute)

    category = SubCategory.objects.all()
    

    if request.method == 'POST':

        poststitle = request.POST.get('poststitle')
        postscat = request.POST.get('postscat')
        postsummary = request.POST.get('postsummary')
        postbody = request.POST.get('postbody')
        postid = request.POST.get('postscat')

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

                    postname = SubCategory.objects.get(pk=postid).name

                    b = Posts(name = poststitle, short_txt = postsummary, body_txt = postbody, date = today, img = filename, imgurl = url, author = "-", 
                                catname = postname, catid = postid, views = 0, time = time)
                    b.save()
                    return redirect('posts_list')

                else:

                    fs = FileSystemStorage()
                    fs.delete(filename)

                    error = "Your File is Larger than 5 MB"
                    return render(request, 'back/error.html', {'error':error})
            
            else:

                fs = FileSystemStorage()
                fs.delete(filename)

                # Come back to lecture 148
                error = "Your File is Not Supported"
                return render(request, 'back/error.html', {'error':error})

        except:

            error = "Please Input Your Content"
            return render(request, 'back/error.html', {'error':error})
    
    return render(request, 'back/posts_add.html', {'category':category})


def posts_delete(request, pk):

    try:

        b = Posts.objects.get(pk=pk)

        fs = FileSystemStorage()
        fs.delete(b.img)

        b.delete()

    except:

        error = "Something Went Wrong"
        return render(request, 'back/error.html', {'error':error})

    return redirect('posts_list')