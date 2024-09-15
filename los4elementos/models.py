from django.db import models

class Partida(models.Model):
    cod_partida = models.CharField(max_length=100, null=True)

    fecha_creacion = models.DateTimeField(null=True)
    fecha_inicio = models.DateTimeField(null=True)
    
    nombre_jugador_1 = models.CharField(max_length=100, null=True)
    nombre_jugador_2 = models.CharField(max_length=100, null=True)
    nombre_jugador_3 = models.CharField(max_length=100, null=True)
    nombre_anfitrion = models.CharField(max_length=100, null=True)
    
    hora_fin_jugador1 = models.DateTimeField(null=True)
    hora_fin_jugador2 = models.DateTimeField(null=True)
    hora_fin_jugador3 = models.DateTimeField(null=True)
    hora_fin_anfitrion = models.DateTimeField(null=True)

class LineaChat(models.Model):
    fecha_hora = models.DateTimeField(null=True)
    nombre_jugador = models.CharField(max_length=100, null=True)
    texto = models.CharField(max_length=500, null=True)




# ====================================
# Create your models here.
class Curso(models.Model):
    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
    nombre = models.CharField(max_length=200, null=True)
    apellidos = models.CharField(max_length=200, null=True)
    fecha_nacimiento = models.DateTimeField(null=True)
    foto = models.CharField(max_length=100, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True)

class Asignatura(models.Model):
    def __str__(self):
        return self.nombre
    
    nombre = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True)
