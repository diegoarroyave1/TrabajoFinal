from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Mensajes tipo cookie temporales
from django.contrib import messages

#Gestión de Errores de base de datos
from django.db import IntegrityError
from .fomrs import EventoForm
from .models import Evento

def inicio(request):
    return render(request, 'paginas/inicio.html')

def eventos(request):
    return render(request, 'eventos/listarEvento.html')

def formularioEvento(request):
    return render(request, 'FFA/evento/crearEvento.html')

def guardarEvento(request):
    try:
        if request.method == "POST":
            q = Evento(
                nombre_evento = request.POST["nombre_evento"],
                fecha_inicio = request.POST["fecha_inicio"],
                feha_fin = request.POST["feha_fin"],
                ubicacion = request.POST["ubicacion"],
                precio = request.POST["precio"],
                Municipio = request.POST["Municipio"],      
            )
            q.save()
            messages.success(request, "Evento guardado correctamente!!")
        else:
            messages.warning(request, "Usted no ha enviado datos...")
    except Exception as e:
        messages.error(request, f"Error: {e}")


