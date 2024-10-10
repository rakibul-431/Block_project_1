# from django.shortcuts import render
# from post.models import post
# from categories.models import category
# def home(request,category_slug=None):
#     data=post.objects.all()
#     if category_slug is not None:
#         category=category.objects.get(slug=category_slug)
#         data=post.objects.filter(category=category)
#     categories=category.objects.all()
#     return render(request,'home.html',{'data':data,'category':categories})

from django.shortcuts import render
from post.models import post
from categories.models import Category
def home(request,category_slug=None):
    model=post.objects.all()
    print(model)
    if category_slug is not None:
        category=Category.objects.get(slug=category_slug)
        model=post.objects.filter(category=category)
    category=Category.objects.all()
    return render(request,'home.html',{'form':model ,'data': category})
    # return render(request,'home.html',{'form':data,'data':catagories})