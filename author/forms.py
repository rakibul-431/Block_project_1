from django import forms
from author.models import author

class author_form(forms.ModelForm):
    class Meta:
        model=author
        fields='__all__'
