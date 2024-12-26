from django import forms
from .models import ArticlePost, Category, Comment

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ['title', 'content', 'author', 'category', 'image']

    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        db_table = 'comment'
        fields = ['author', 'content']