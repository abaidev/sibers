from django import forms
from .models import Post, Image


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class PostImageForm(PostForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta(PostForm.Meta):
        fields = PostForm.Meta.fields + ['images']