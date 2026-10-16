
from django.urls import path
from .views import nuevoHello, bye, edad, primer_plantilla, segunda_plantilla, tercer_plantilla, cuarta_plantilla, crear_musico, crear_album, crear_autor, crear_lector, crear_libro
urlpatterns = [

    path('hello', nuevoHello ),
    
    path('bye', bye),
    
    #path('edad/<int:edad>', edad),
    
    path('edad/<int:edad>/<int:futuro>', edad),
    
    path('plantilla1', primer_plantilla),
    
    path('plantilla2', segunda_plantilla),
    
    path('plantilla3', tercer_plantilla),
    
    path('plantilla4', cuarta_plantilla),
    
    path('crear_musico/<str:nombre>/<str:apellido>/<str:instrumento>', crear_musico),
    
    path('crear_album/<str:nombre>/<int:estrellas>/<int:artista_id>' , crear_album),
    
    path('crear_autor/<str:nombre>/<str:apellido>', crear_autor),
    
    path('crear_lector/<str:nombre>/<str:apellido>/<str:email>', crear_lector),
    path('crear_libro/<str:titulo>/<int:anio>/<int:autor_id>', crear_libro),
    
    ]

