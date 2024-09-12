from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from django.db.models import Q

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
            return redirect("/los4elementos/start/anfitrion/" + nombre_jugador + "/@")

        if "invitado" in request.POST:
            codigo_partida = request.POST.get("codigo_partida")

            # Comprobar que hay codigo de partida
            if not codigo_partida or codigo_partida == "":
                contexto = { "error" : "El código de la partida es obligatorio para entrar en privado" }
                return render(request, "ingresar-partida.html", contexto)

            return redirect("/los4elementos/start/invitado/" + nombre_jugador + "/" + codigo_partida)
        else:
            return redirect("/los4elementos")

    else:
        return render(request, "ingresar-partida.html", contexto)

def start(request, tipo_jugador, nombre_jugador, codigo_partida):
    contexto = {
        "tipo_jugador" : tipo_jugador,
        "nombre_jugador" : nombre_jugador,
        "codigo_partida" : codigo_partida
    }

    return render(request, "start.html", contexto)
