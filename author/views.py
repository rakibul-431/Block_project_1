from django.shortcuts import render,redirect
from author.forms import author_form

# Create your views here.
def add_author(request):
    if request.method=='POST':
      form_author=author_form(request.POST)
      if form_author.is_valid():
          form_author.save()
          return redirect('add_author')
    else:
       form_author=author_form()
       return render(request,'author/add_author.html',{'author':form_author})
