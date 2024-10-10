from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

# class author_form(forms.ModelForm):
#     class Meta:
#         model=author
#         fields='__all__'

class RejistrationForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
class ChangeUserdata(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']