
from django.urls import path
from .views import nuevoHello, bye, edad, primer_plantilla
urlpatterns = [

    path('hello', nuevoHello ),
    
    path('bye', bye),
    
    #path('edad/<int:edad>', edad),
    
    path('edad/<int:edad>/<int:futuro>', edad),
    
    path('plantilla', primer_plantilla),
]
