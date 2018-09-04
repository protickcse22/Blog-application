from django import forms
from . import models

class CreateArticleform(forms.ModelForm):
    class Meta:
        model=models.Article
        fields = ['title','body','slug','thumb']


