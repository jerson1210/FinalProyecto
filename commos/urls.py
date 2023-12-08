from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='app'),
    path('noticia/',views.noticia, name='noticia'),
    path('registrarNoticia/',views.registrarNoticia),
    path('nike/', views.nike, name='nike'),
    path('adidas/', views.adidas, name='adidas'),
    path('vans/', views.vans, name='vans'),
    path('otros/',views.otros, name='otros'),
    path('borrar/<codigo>',views.borrar,name='borrar'),
    path('ver/<codigo>',views.ver,name='ver'),
    path('editarNoticia/',views.editarNoticia,name='editarNoticia'),
    path('edicion/<int:codigo>',views.edicion,name='edicion'),
    path('registrar/',views.registrar)
]