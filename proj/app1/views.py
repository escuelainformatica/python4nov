from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect

from app1.modelos.categoria import Categoria
from app1.models import Autor, Articulo

def listar_articulo(request:HttpRequest):
    articulos=list(Articulo.objects.all())
    return render(request,'listar_articulo.html',{'articulos':articulos})

# Create your views here.
def agregar_articulo(request:HttpRequest):
    boton=request.POST.get('boton','')

    autor=Autor(id=request.POST.get('autor',''))
    cat=Categoria(request.POST.get('categoria',''))
    articulo=Articulo(
        titulo=request.POST.get('titulo',''),
        contenido=request.POST.get('contenido', ''),
        autor=autor,
        categoria=cat
    )
    autores=Autor.objects.all()
    categorias=Categoria.objects.all()
    if boton!="": # se presiono el boton
        # pass  # indicar que no se haga nada.
        articulo.save()
        return redirect('/listar_articulo')
    else:
        return render(request,"agregar_articulo.html",{"articulo":articulo,"autores":autores,'categorias':categorias})
