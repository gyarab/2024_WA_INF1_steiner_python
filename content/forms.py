from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='Nick', max_length=100)
    text = forms.CharField(label='Co na to říkáte?', widget=forms.Textarea)