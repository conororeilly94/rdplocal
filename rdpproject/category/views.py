from django.shortcuts import render, get_object_or_404, redirect
from .models import Category

# Create your views here.

def cat_list(request):

    # Authenticating user
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # End login check

    category = Category.objects.all()
    return render(request, 'back/category_list.html', {'category':category})


def cat_add(request):

    # Authenticating user
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # End login check

    if request.method == 'POST':

        name = request.POST.get('name')

        if name == "":

            error = "You Must Enter a Title"
            return render(request, 'back/error.html', {'error':error})

        if len(Category.objects.filter(name=name)) != 0:

            error = "This Category Already Exists"
            return render(request, 'back/error.html', {'error':error})

        b = Category(name=name)
        b.save()
        return redirect('cat_list')
        
    return render(request, 'back/category_add.html')


def cat_del(request, pk):

    # Authenticating user
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # End login check

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0:
        a = Category.objects.get(pk=pk).author
        if str(a) != str(request.user):
            error = "Access Denied"
            return render(request, 'back/error.html', {'error':error})

    category = Category.objects.filter(pk=pk)
    category.delete()

    return redirect('cat_list')

