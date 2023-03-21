"""mi_primer_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hola_mundo.views import saludar, saludar_a, sumar, mostrar_mis_tareas
from SocialTravel.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola-mundo/saludar', saludar),
    path('hola-mundo/suludar-a/<alguien>', saludar_a),
    path('hola-mundo/sumar/<int:a>/<int:b>', sumar),
    path('mis-tareas/<criterio>', mostrar_mis_tareas, name="mis-tareas"),
    path('', index),
]
