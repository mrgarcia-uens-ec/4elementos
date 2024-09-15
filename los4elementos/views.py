from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from django.db.models import Q

from .models import Partida

import random
import datetime

def index(request):
    contexto = { }
    return render(request, "inicio.html", contexto)

def ingresar_partida(request):
    contexto = { }

    if request.method == 'POST':
        nombre_jugador = request.POST.get("nombre_jugador")
        if "atras" in request.POST:
            print("atras")
            return redirect("/los4elementos")
        else:
            if not nombre_jugador or nombre_jugador == "":
                contexto = { "error" : "El nombre del jugador es obligatorio" }
                return render(request, "ingresar-partida.html", contexto)
        
        if "anfitrion" in request.POST:
            # Crear el código como un número aleatorio de 6 cifras
            codigo_partida = str(random.randint(100000, 999999))

            # Crear la partida en la BD
            partida = Partida.objects.create(
                cod_partida=codigo_partida,
                fecha_creacion=datetime.datetime.now(),
                nombre_anfitrion = nombre_jugador
            )
            
            return redirect("/los4elementos/start/anfitrion/" + nombre_jugador + "/" + codigo_partida)

        if "invitado" in request.POST:
            codigo_partida = request.POST.get("codigo_partida")

            # Comprobar que hay codigo de partida
            if not codigo_partida or codigo_partida == "":
                contexto = { "error" : "El código de la partida es obligatorio para entrar en privado" }
                return render(request, "ingresar-partida.html", contexto)

            # Comprobar que existe el código de partida
            partida_obj = Partida.objects.filter(cod_partida = codigo_partida)
            if not partida_obj:
                contexto = { "error" : "El código de partida no existe" }            
                return render(request, "ingresar-partida.html", contexto)
            
            partida = partida_obj.get()

            if not partida.nombre_jugador_1 or partida.nombre_jugador_1 == "":
                partida_obj.update(nombre_jugador_1=nombre_jugador)
            elif not partida.nombre_jugador_2 or partida.nombre_jugador_2 == "":
                partida_obj.update(nombre_jugador_2=nombre_jugador)
            elif not partida.nombre_jugador_3 or partida.nombre_jugador_3 == "":
                partida_obj.update(nombre_jugador_3=nombre_jugador)
            else:
                contexto = { "error" : "Ya no hay espacio para otro jugador" }
                return render(request, "ingresar-partida.html", contexto)

            return redirect("/los4elementos/start/invitado/" + nombre_jugador + "/" + codigo_partida)
        else:
            return redirect("/los4elementos")

    else:
        return render(request, "ingresar-partida.html", contexto)

def start(request, tipo_jugador, nombre_jugador, codigo_partida):
    # Obtener la partida
    partida = Partida.objects.filter(cod_partida = codigo_partida)
    
    contexto = {
        "partida" : partida.get(),
        "tipo_jugador" : tipo_jugador,
        "nombre_jugador" : nombre_jugador,
        "codigo_partida" : codigo_partida
    }

    if request.method == 'POST':
        partida.update(fecha_inicio=datetime.datetime.now())
        return redirect("/los4elementos/partida")
    else:
        return render(request, "start.html", contexto)
    
def partida(request):
    return render(request, "partida.html")
