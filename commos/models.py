from django.db import models
from django.contrib.auth.models import User


class Noti(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    titulo = models.TextField()
    usuario = models.ForeignKey(User,  null=True, blank=True, on_delete=models.CASCADE)
    CATEGORIA_CHOICES = [
        ('Nike', 'Nike'),
        ('Adidas', 'Adidas'),
        ('Vans', 'Vans'),
        ('Otros', 'Otros'),
    ]
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, default='Otros')
    parrafo = models.TextField()
    noticial = models.TextField()
    imagen = models.FileField(upload_to="noticas/")

    
