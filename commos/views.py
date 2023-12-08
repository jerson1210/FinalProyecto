from django.shortcuts import render, redirect
from .models import Noti
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    # Consultar noticias
    noticias_list = Noti.objects.all()

    # Configurar paginación cada 6 noticias
    paginator = Paginator(noticias_list,8)

    # Obtener página
    page_number = int(request.GET.get('page', 1)) 
    page_obj = paginator.get_page(page_number)

    # Renderizar la plantilla con el contexto
    return render(request, "index.html", {"noticia": page_obj})


def nike(request):
    # Consultar noticias con la categoría 'Nike'
    noticias_list = Noti.objects.filter(categoria='Nike')

    # Configurar paginación cada 9 noticias
    paginator = Paginator(noticias_list, 4)

    # Obtener página
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Renderizar la plantilla con el contexto
    return render(request, 'nike.html', {'noticia': page_obj})

def adidas(request):
    # Consultar noticias con la categoría 'Nike'
    noticias_list = Noti.objects.filter(categoria='Adidas')

    # Configurar paginación cada 9 noticias
    paginator = Paginator(noticias_list, 9)

    # Obtener página
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Renderizar la plantilla con el contexto
    return render(request, 'adidas.html', {'noticia': page_obj})


def vans(request):
     # Consultar noticias con la categoría 'Nike'
    noticias_list = Noti.objects.filter(categoria='Vans')

    # Configurar paginación cada 9 noticias
    paginator = Paginator(noticias_list, 9)

    # Obtener página
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Renderizar la plantilla con el contexto
    return render(request, 'vans.html', {'noticia': page_obj})

def otros(request):
     # Consultar noticias con la categoría 'Nike'
    noticias_list = Noti.objects.filter(categoria='Otros')

    # Configurar paginación cada 9 noticias
    paginator = Paginator(noticias_list, 9)

    # Obtener página
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Renderizar la plantilla con el contexto
    return render(request, 'otros.html', {'noticia': page_obj})


def registrar(request):
    return render(request,"NuevaNota.html")

def registrarNoticia(request):
    mensaje_error = None

    if request.method == 'POST':
        codigo = request.POST['codigo']
        titulo = request.POST['titulo']
        parrafo = request.POST['parrafo']
        categoria=request.POST['categoria']
        noticial = request.POST['noticial']
        usuario = request.user
        imagen= request.FILES['imagen']

        # Verifica si ya existe un registro con el mismo código
        existe_registro = Noti.objects.filter(titulo=titulo).exists()
        existe_registro = Noti.objects.filter(codigo=codigo).exists()

        if not existe_registro:
            # Si no existe, crea el nuevo registro
            noticia = Noti.objects.create(codigo=codigo, titulo=titulo, usuario=usuario ,parrafo=parrafo, categoria=categoria,noticial=noticial , imagen=imagen)
            return redirect('noticia')
        else:
            # Si ya existe un registro con el mismo código, muestra un mensaje de error
            mensaje_error = f"Ya existe un registro con el código {codigo}. Intente con otro código."
            

    # Renderiza la plantilla con el mensaje de error
    return render(request, 'noticia.html', {'mensaje_error': mensaje_error})

def noticia(request):
    # Consultar noticias
    noticia = Noti.objects.filter(usuario=request.user)

     # Renderizar la plantilla con el contexto
    return render(request, "noticia.html", {"noticia": noticia})
  
def borrar(request,codigo):

    noticia=Noti.objects.get(codigo=codigo)
    noticia.delete()
    return redirect('noticia')

def ver(request,codigo):
    noticia = Noti.objects.get(codigo=codigo)
    return render(request,"ver.html",{"noticia":noticia})

def edicion(request,codigo):
    noticia = Noti.objects.get(codigo=codigo)
    return render(request,"edicion.html",{"noticia":noticia})

def editarNoticia(request):
    codigo = request.POST['codigo']
    titulo = request.POST['titulo']
    parrafo = request.POST['parrafo']
    categoria = request.POST['categoria']
    noticial = request.POST['noticial']
    usuario = request.user
    nueva_imagen = request.FILES.get('imagen')  # Obtén la nueva imagen de la solicitud

    noticia = Noti.objects.get(codigo=codigo)
    noticia.titulo = titulo
    noticia.parrafo = parrafo
    noticia.categoria = categoria
    noticia.noticial = noticial
    
    # Verificar si se proporcionó una nueva imagen
    if nueva_imagen:
        noticia.imagen = nueva_imagen

    noticia.save()

    return redirect('noticia')

