from django.shortcuts import render
from django.http import HttpResponse
from hola_mundo.models import Tarea

def saludar(request):
    return HttpResponse("Hola Mundo !!")

def saludar_a(request, alguien):
    return HttpResponse(f"Hola como estas {alguien.title()}")


def sumar(request, a, b):
    return HttpResponse(f"El resultado de {a} + {b} = {a+b}")


def mostrar_mis_tareas(request, criterio):
    tareas = Tarea.objects.filter(nombre=criterio).all()
    return render(request, "hola_mundo/tareas.html", {"tareas": tareas})
