from django import forms
from profiles.models import profile

class add_profile(forms.ModelForm):
    class Meta:
        model=profile
        fields='__all__'