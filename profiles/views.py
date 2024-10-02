from django.shortcuts import render,redirect
from profiles.forms import add_profile

# Create your views here.
def profile_add(request):
    if request.method=='POST':
       profil=add_profile(request.POST)
       if profil.is_valid():
           profil.save()
           return redirect('add_profile')
    else:
        profil=add_profile()
        return render(request,'add_profile.html',{'profil':profil})
