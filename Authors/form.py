from django import forms
from .models import Authors

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ["authorName","phoneNumber","img"]
