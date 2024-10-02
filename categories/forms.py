from django import forms
from categories.models import categories

class creat_catagory(forms.ModelForm):
    class Meta:
        model=categories
        fields='__all__'