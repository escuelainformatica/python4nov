from django.db import models
from app1.modelos.categoria import Categoria


# Create your models here.

class Autor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)


class Articulo(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=2000)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
