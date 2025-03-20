from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='Vase jmeno', max_length=100)
    text = forms.CharField(label='Komentar', widget=forms.Textarea)