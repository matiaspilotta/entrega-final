from django import forms
from .models import Avatar
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel


class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["username","email","password1", "password2"]
        help_texts = {k: "" for k in fields}


class UserEditionFormulario(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)


    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}


class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen"]


class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()


