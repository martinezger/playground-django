from django.shortcuts import render
from django.http import HttpResponse
from hola_mundo.models import Tarea, Persona
from hola_mundo.forms import BuscarPersonasForm
from django.views.generic import ListView

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
    "total_personas":total_personas,
    "form": BuscarPersonasForm(),
    })


class BuscarPersona(ListView):
    model = Persona
    context_object_name = "personas"

    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
           return Persona.objects.filter(nombre__icontains=f.data.get("criterio_nombre")).all()
        return Persona.objects.all()

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form'] =  BuscarPersonasForm(self.request.GET)
        return context



def buscar_personas(request):
    f = BuscarPersonasForm(request.GET)
    context = {
        "personas": None,
        "form": f
    }
    if f.is_valid():
        context["personas"] = Persona.objects.filter(nombre__icontains=f.data.get("criterio_nombre")).all()
    return render(request, "hola_mundo/personas.html", context)
