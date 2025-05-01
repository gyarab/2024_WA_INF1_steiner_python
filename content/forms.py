from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Field

class CommentForm(forms.Form):
    name = forms.CharField(label='Nick', max_length=100)
    text = forms.CharField(label='Co na to říkáte?', widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(label='Uživatelské jméno', max_length=100)
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('username'),
                Field('password'),
            ),
            Submit('submit', 'Přihlásit se', css_class='btn-primary')
        )  

class LogoutForm(forms.Form):
    confirm = forms.BooleanField(label="Opravdu se chcete odhlásit?")


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('email'),
                Field('username'),
                Field('password1'),
                Field('password2'),
            ),            
            Submit('submit', 'Vytvořit účet', css_class='btn-primary')
        )