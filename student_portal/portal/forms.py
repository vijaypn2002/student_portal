from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    roll_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    captcha = CaptchaField()