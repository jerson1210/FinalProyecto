from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm  # Asegúrate de importar tu formulario SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def hola(request):
    if request.method == 'GET':
        print('Enviando formulario') 
        return render(request, 'singup.html', {
            'form': SignUpForm()  # Usa una instancia del formulario, no la clase directamente
        })
    else:
        form = SignUpForm(request.POST)
        if form.is_valid() and form.cleaned_data['password1'] == form.cleaned_data['password2']:
            try:
                user = form.save()
                login(request, user)
                return redirect('app')
            except:
                return render(request, 'singup.html', {
                    'form': SignUpForm(),
                    "error": 'Usuario ya existe'
                })
        return render(request, 'singup.html', {
            'form': SignUpForm(),
            "error": 'Contraseña no coincide'
        })

def signout(request):
    logout(request)
    return redirect('app')

def sigin(request):
    if request.method == 'GET':
        return render(request, 'home.html', {
            'form': AuthenticationForm
        })
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('app')
        return render(request, 'home.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña no válidos'
        })

