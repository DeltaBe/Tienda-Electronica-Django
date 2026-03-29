from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dispositivo
from .cart import Carrito

# Create your views here.


def home(request):
    productos = Dispositivo.objects.all()
    return render(request, 'index.html', {'productos': productos})

def agregar_producto(request, id):
    carrito = Carrito(request)
    producto = get_object_or_404(Dispositivo, id=id)
    carrito.agregar(producto)
    return redirect('home')

def detalle_carrito(request):
    return render(request, 'carrito.html')

def eliminar_del_carrito(request, id):
    carrito = Carrito(request)
    producto = get_object_or_404(Dispositivo, id=id)
    carrito.eliminar(producto)
    return redirect('detalle_carrito')