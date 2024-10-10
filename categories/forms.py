from django import forms
from categories.models import Category

class creat_catagory(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'