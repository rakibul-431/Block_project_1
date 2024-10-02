from django.shortcuts import render,redirect
from categories.forms import creat_catagory

# Create your views here.
def categorys(request):
    if request.method=='POST':
       cata=creat_catagory(request.POST)
       if cata.is_valid():
           cata.save()
           return redirect('catagorys')
    else:
        cata=creat_catagory()
        return render(request,'category.html',{'categorys':cata})
