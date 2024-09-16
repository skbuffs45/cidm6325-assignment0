from django import forms
from .models import Comment, Rating

class EmailRecipeForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

class CommentForm(forms.ModelForm):
     class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class SearchForm(forms.Form):
    query = forms.CharField()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['subject', 'review', 'rating']