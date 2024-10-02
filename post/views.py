from django.shortcuts import render,redirect
from post.forms import creat_post
from post import models

# Create your views here.
def post(request):
    if request.method=='POST':
       add_post=creat_post(request.POST)
       if add_post.is_valid():
           add_post.save()
           return redirect('post')
    else:
        add_post=creat_post()
        return render(request,'post.html',{'pst':add_post})



def edit_post(request,id):
    post=models.post.objects.get(pk=id)
    add_post=creat_post(instance=post)
    if request.method=='POST':
       add_post=creat_post(request.POST,instance=post)
       if add_post.is_valid():
           add_post.save()
           return redirect('homepage')
    
    return render(request,'post.html',{'pst':add_post})

def post_delete(request,id):
    post=models.post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')