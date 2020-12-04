from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)
    confirm_code = forms.CharField(required=True)
    # phone = forms.CharField(required=True)
    name = forms.CharField(required=True)

    def save(self, *args, **kwargs):
        user = User(first_name=self.cleaned_data["name"],
                    email=self.cleaned_data["email"],
                    password=self.cleaned_data["password"])
        user.save()
