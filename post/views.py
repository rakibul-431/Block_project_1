from django.shortcuts import render,redirect
from post.forms import creat_post,CommentForm
from post import models
from post.models import post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

# Create your views here.
@login_required
def post(request):
    if request.method=='POST':
       add_post=creat_post(request.POST)
       if add_post.is_valid():
        #    add_post.cleaned_data['author']=request.user
           add_post.instance.author=request.user
           add_post.save()
           return redirect('post')
    else:
        add_post=creat_post()
        return render(request,'post.html',{'pst':add_post})
    

#Add post by class base view
# class AddPostCreatView(CreateView):
#     model=models.post
#     form_class=creat_post
#     template_name='post.html'
#     success_url=reverse_lazy('post')
#     def form_valid(self, form):
#         form.instance.author=self.request.user
#         return super().form_valid(form)
        



@login_required
def edit_post(request,id):
    post=models.post.objects.get(pk=id)
    add_post=creat_post(instance=post)
    if request.method=='POST':
       add_post=creat_post(request.POST,instance=post)
       if add_post.is_valid():
           add_post.save()
           return redirect('homepage')
    
    return render(request,'post.html',{'pst':add_post})

#Update by class base view
class updatePost(UpdateView):
    model=models.post
    form_class=creat_post
    template_name='post.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('homepage')


@login_required
def post_delete(request,id):
    post=models.post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

#Delete post by use class base view

class deletepost(DeleteView):
    model=models.post
    template_name='delete.html'
    success_url=reverse_lazy('profile_page')
    pk_url_kwarg='id'



class DetailsView(DetailView):
    model=models.post
    template_name='details.html'
    pk_url_kwarg='id'  
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs) 
        post=self.objects
        comments=post.comments
        if self.request.method=='POST':
            comment_form=forms.CommentForm(data=self.request.POST)
            if comment_form.is_valid():
                new_comment=comment_form.save(commit=False)
                new_comment.post=post
                new_comment.save()
        else:
            comment_form=forms.CommentForm()
        context['comments']=comments
        context['comment_form']=comment_form
        return context
    

