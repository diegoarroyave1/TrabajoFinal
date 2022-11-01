from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Login(models.Model):
    id_usuario = models.CharField(max_length=50, blank=False, null=False)


    def __str__(self):
        return f"{self.id_usuario} - {self.id_usuario}"

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True) 
    primer_nombre = models.CharField(max_length=20, blank=False, null=False)
    segundo_nombre = models.CharField(max_length=20, blank=False, null=False)
    primer_apellido =models.CharField(max_length=20, blank=False, null=False)
    segundo_apellido = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField( blank=False, null=False, unique=True)
    fecha_de_nacimiento = models.DateTimeField( auto_now_add=True)



    def __str__(self):
        return f"{self.primer_nombre} - {self.segundo_apellido}"

class Invitaciones(models.Model):
    id_invitaciones = models.AutoField(primary_key=True) 
    nombre_invitacion = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField( blank=False, null=False, unique=True)
    
    def __str__(self):
        return f"{self.id_invitaciones}"

class Liga(models.Model):
    id_liga = models.AutoField(primary_key=True) 
    nombre_liga = models.CharField(max_length=20, blank=False, null=False, unique=True)

    
    def __str__(self):
        return f"{self.id_liga} - {self.nombre_liga}"

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre_evento = models.CharField(max_length=15, blank=False, null=False, unique=True)
    fecha_inicio =  models.DateTimeField( auto_now_add=True)
    feha_fin =  models.DateTimeField( auto_now_add=True)
    ubicacion = models.CharField(max_length=15, blank=False, null=False)
    precio = models.IntegerField(null=False, blank=False)
    Municipio= models.CharField(max_length=15, blank=False, null=False, unique=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    id_liga = models.ForeignKey(Liga, on_delete=models.DO_NOTHING)
    id_invitaciones = models.ForeignKey(Invitaciones, on_delete=models.DO_NOTHING, null=True, blank=True)



    def __str__(self):
        return f"{self.nombre_evento} - {self.fecha_inicio} - {self.feha_fin}  - {self.ubicacion} - {self.precio} - {self.Municipio}"



class Comentarios(models.Model):
    id_comentarios = models.CharField(max_length=15,primary_key=True)
    Comentarios = models.CharField(max_length=15, blank=False, null=False)
    fecha_ingreso = models.DateTimeField( auto_now_add=True)
    hora_ingreso = models.DateTimeField( auto_now_add=True)
    id_evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.id_comentarios} - {self.Comentarios}"



