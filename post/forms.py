from django import forms
from post.models import post

class creat_post(forms.ModelForm):
    class Meta:
        model=post
        fields='__all__'