from multiprocessing import Event
from django.contrib import admin
from .models import Login, Usuarios, Evento, Liga, Comentarios, Invitaciones
# Register your models here.

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id_usuario',)
    search_fields = ['nombre', 'cedula']


@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'fecha_de_nacimiento')
    search_fields = ['nombre', 'cedula']

@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
    list_display = ('id_liga', 'nombre_liga', )
    search_fields = ['nombre', 'cedula']

@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('id_comentarios', 'Comentarios', 'fecha_ingreso', 'hora_ingreso', )
    search_fields = ['nombre', 'cedula']


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id_evento', 'nombre_evento', 'fecha_inicio', 'feha_fin', 'precio', 'Municipio','id_usuario','id_liga','id_invitaciones')
    search_fields = ['nombre', 'cedula']

@admin.register(Invitaciones)
class InvitacionesAdmin(admin.ModelAdmin):
    list_display = ('id_invitaciones', 'nombre_invitacion', 'email', )
    search_fields = ['nombre', 'cedula']    
