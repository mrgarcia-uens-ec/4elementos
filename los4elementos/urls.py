from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ingresar-partida", views.ingresar_partida, name="ingresar_partida"),
    path("start/<str:tipo_jugador>/<str:nombre_jugador>/<str:codigo_partida>", views.start, name="start"),
    path("partida", views.partida, name="partida"),
]