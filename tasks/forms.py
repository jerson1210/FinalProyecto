# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text='Requerido. Ingresa una dirección de correo válida.')

    class Meta:
        model = User  # Suponiendo que estás utilizando el modelo User de django.contrib.auth.models
        fields = ('full_name', 'email', 'username', 'password1', 'password2')
