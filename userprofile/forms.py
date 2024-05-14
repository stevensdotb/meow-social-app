from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout

from .models import Post


class PostForm(forms.Form):
    text = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"placeholder": "What's your thoughts?", "rows": 3, "maxlength": 140}),
        max_length=140
    )

    class Meta:
        model = Post
        fields = ("text")
