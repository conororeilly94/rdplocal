# ACTIONS
from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from posts.models import Posts
from category.models import Category
from subcategory.models import SubCategory
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):

    site = Main.objects.get(pk=2)
    posts = Posts.objects.all().order_by('-pk')
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    lastposts = Posts.objects.all().order_by('-pk')[:3]

    return render(request, 'front/home.html', {'site':site, 'posts':posts, 'category':category, 'subcategory':subcategory, 'lastposts':lastposts})
    
def about(request):

    site = Main.objects.get(pk=2)

    return render(request, 'front/about.html', {'site':site})


def panel(request):

    # Authenticating user
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # End login check

    return render(request, 'back/home.html')


def mylogin(request):

    if request.method == 'POST':

        # 182
        uuser = request.POST.get('username')
        upassword = request.POST.get('password')

        if uuser != "" and upassword != "":

            user = authenticate(username = uuser, password = upassword)

            if user != None:

                login(request, user)
                return redirect('panel')

    return render(request, 'front/login.html')


def mylogout(request):

    logout(request)

    return redirect('mylogin')