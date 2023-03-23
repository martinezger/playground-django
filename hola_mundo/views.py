from django.shortcuts import render
from django.http import HttpResponse
from hola_mundo.models import Tarea, Persona

def saludar(request):
    return HttpResponse("Hola Mundo !!")

def saludar_a(request, alguien):
    return HttpResponse(f"Hola como estas {alguien.title()}")


def sumar(request, a, b):
    return HttpResponse(f"El resultado de {a} + {b} = {a+b}")


def mostrar_mis_tareas(request, criterio):
    
    if criterio == "todo":
        tareas = Tarea.objects.all()
    else:
        tareas = Tarea.objects.filter(nombre=criterio).all()

    return render(request, "hola_mundo/tareas.html", {"tareas": tareas})


def mostrar_personas(request):

    personas = Persona.objects.all()
    total_personas = len(personas)
    return render(request, "hola_mundo/personas.html", 
    {"personas": personas, 
    "total_personas":total_personas
    })