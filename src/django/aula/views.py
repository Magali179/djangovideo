""" from django.shortcuts import render"""
from django.http import HttpResponse
from datetime import date
from django.template import Template, Context
# Create your views here.

'''funcion que devuelve un saludo, recibe request como primer parametro'''
def nuevoHello(request):
    return HttpResponse("Hola mundo!!!")

def bye(request):
    return HttpResponse("Hasta luego!!")

'''pasamos 2 parametros, request y edad'''
def edad(request, edad, futuro):
    incremento = futuro - date.today().year
    mensaje = "En el anio %d cumpliras %d anios" % (futuro, edad + incremento)
    return HttpResponse(mensaje)

def primer_plantilla(request):
    
    plantilla = """
    <html>
        <body>
            <h2>
                Hola! {{nombre}}, esta es mi primer plantilla!
            </h2>
        </body>
    </html>"""
    
    
    tpl = Template(plantilla)
    
    ctx = Context({
        'nombre': 'Juan perez'
    })
    
    mensaje = tpl.render(ctx)
    
    return HttpResponse(mensaje)