from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCategory
from category.models import Category

# Create your views here.

def subcat_list(request):

    # Authenticating user
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # End login check

    subcategory = SubCategory.objects.all()
    return render(request, 'back/subcategory_list.html', {'subcategory':subcategory})


def subcat_add(request):

    # Authenticating user
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # End login check

    category = Category.objects.all()

    if request.method == 'POST':

        name = request.POST.get('name')
        catid = request.POST.get('category')

        if name == "":

            error = "You Must Enter a Title"
            return render(request, 'back/error.html', {'error':error})

        # if len(SubCategory.objects.filter(name=name)) != 0:

        #     error = "This Category Already Exists"
        #     return render(request, 'back/error.html', {'error':error})

        catname = Category.objects.get(pk=catid).name

        b = SubCategory(name=name, catname=catname, catid=catid)
        b.save()
        return redirect('subcat_list')
        
    return render(request, 'back/subcategory_add.html', {'category':category})


def subcat_del(request, pk):
    
    # Authenticating user
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # End login check

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0:
        a = SubCategory.objects.get(pk=pk).author
        if str(a) != str(request.user):
            error = "Access Denied"
            return render(request, 'back/error.html', {'error':error})

    subcategory = SubCategory.objects.filter(pk=pk)
    subcategory.delete()

    return redirect('subcat_list')