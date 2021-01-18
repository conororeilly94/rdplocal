from django.shortcuts import render, get_object_or_404, redirect
from .models import Category

# Create your views here.

def cat_list(request):


    category = Category.objects.all()
    return render(request, 'back/category_list.html', {'category':category})


def cat_add(request):   

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