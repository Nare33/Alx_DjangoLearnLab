from django import forms
from .models import Comment
from .models import Post, Tag
from taggit.forms import TagWidget
from django.forms import widgets

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    title = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=widgets.Textarea(attrs={'class': 'form-control'}))
    tags = forms.CharField(widget=TagWidget(), required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows': 4})

