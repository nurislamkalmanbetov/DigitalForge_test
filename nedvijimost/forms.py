from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class": "form-control form-control-lg", "placeholder": "email"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "type": "password",
                "autocomplete": "off",
                "placeholder": "Пароль"
            }
        )
    )
