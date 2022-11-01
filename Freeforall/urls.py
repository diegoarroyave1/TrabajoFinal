from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('eventos/', views.eventos, name='eventos'),
    path('evento/crear/', views.guardarEvento, name='guardarEvento'),
    
    


]