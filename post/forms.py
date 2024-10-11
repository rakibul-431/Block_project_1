from django import forms
from post.models import post,Comment

class creat_post(forms.ModelForm):
    class Meta:
        model=post
        # fields='__all__'
        exclude=['author']
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','body']