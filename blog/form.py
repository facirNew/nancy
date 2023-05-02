from django import forms
from pytils.translit import slugify
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_view', 'content', 'photo', 'tags', 'is_published']
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }
