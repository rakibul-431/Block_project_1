from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from author.forms import RejistrationForm,ChangeUserdata
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from post.models import post

# Create your views here.
# def add_author(request):
#     if request.method=='POST':
#       form_author=author_form(request.POST)
#       if form_author.is_valid():
#           form_author.save()
#           return redirect('add_author')
#     else:
#        form_author=author_form()
#        return render(request,'author/add_author.html',{'author':form_author})
def Rejistration(request):
      if request.method=='POST':
        form_author=RejistrationForm(request.POST)
        if form_author.is_valid():
            form_author.save()
            messages.success(request,'Account creat successful')
            return redirect('login_page')
      else:
        form_author=RejistrationForm()
      return render(request,'author/registration.html',{'form':form_author,'type':'Rejister'})

def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=name,password=user_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'Login successful')
                return redirect('profile_page')
            else:
                messages.warning(request,'Login field')
                return redirect('login_page')
    else:
        form=AuthenticationForm()
    return render(request,'author/registration.html',{'form':form,'type':'login'})

@login_required
def profiel(request):
    data=post.objects.filter(author=request.user)
    return render(request,'author/profile.html',{'data':data})


@login_required
def updateprofile(request):
      if request.method=='POST':
        form=ChangeUserdata(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'User updata data successful')
            return redirect('profile_page')
      else:
        form=ChangeUserdata(instance=request.user)
      return render(request,'author/profilechange.html',{'form':form})
@login_required
def UserpasswordChange(request):
      if request.method=='POST':
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'password change successful')
            return redirect('profile_page')
      else:
        form=PasswordChangeForm(user=request.user)
      return render(request,'author/profilechange.html',{'form':form})
def user_logout(request):
    logout(request)
    return redirect('login_page')
    