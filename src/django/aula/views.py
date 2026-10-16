""" from django.shortcuts import render"""
from django.http import HttpResponse
from datetime import date
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from .models import Musico, Album
from .models import Autor, Lector, Libro
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
                Hola! {{ nombre }}, esta es mi primer plantilla!
            </h2>
        </body>
    </html>"""

    tpl = Template(plantilla)

    ctx = Context({
        'nombre': 'Juan Perez',
         
    })

    mensaje = tpl.render(ctx)

    return HttpResponse(mensaje)

def segunda_plantilla(request):
    
       
    tpl = get_template("segunda_plantilla.html")
    
    mensaje = tpl.render({
        'nombre': 'Juan Perez',
        'fecha_actual': date.today()}
    )
    return HttpResponse(mensaje)

def tercer_plantilla(request):
    
    return render(request, "tercer_plantilla.html", {
        'nombre': 'Magali Moreno',
        'fecha_actual': date.today()
    })
    
class Empleado(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
def cuarta_plantilla(request):
    
    empleado =Empleado(nombre="Juan", apellido="Gomez")
    
    laborables = ['lunes', 'martes', 'miecoles', 'jueves', 'viernes', 'sabado', 'domingo']
    
    return render(request, "cuarta_plantilla.html", {
        'mi_empleado': empleado,
        'fecha_actual': date.today(),
        'dias_laborables': laborables
    })
    
       
def crear_musico(request, nombre, apellido,instrumento):
    per=Musico(first_name=nombre, last_name=apellido, instrumento=instrumento)
    per.save()
    mensaje = "Se creo el musico %s %s con ID %d" % (nombre, apellido, per.id)
    return HttpResponse(mensaje)


def crear_album(request, nombre, estrellas, artista_id):
    artista=Musico.objects.get(id=artista_id)
    album=Album(nombre=nombre, fecha_salida=date.today(), estrellas=2, artista=artista)
    album.save()
    mensaje = "Se creo el album %s del artista %s con ID %d" % (nombre, artista.first_name + " " + artista.last_name, album.id)
    return HttpResponse(mensaje)

# practica
def crear_autor(request, nombre, apellido):
    autor = Autor(nombre=nombre, apellido=apellido)
    autor.save()
    mensaje= "Se creo el autor %s, %s"%(nombre, apellido)
    return HttpResponse(mensaje)

def crear_lector(request, nombre, apellido, email):
    lector = Lector(nombre=nombre, apellido=apellido, email=email)
    lector.save()
    mensaje = "Se creo el lector %s, %s y su email %s" %(nombre, apellido, email)
    return HttpResponse(mensaje)

def crear_libro(request, titulo, anio, autor_id):
    autor =Autor.objects.get(id=autor_id)
    libro= Libro(autor=autor, titulo=titulo, anio=anio)
    libro.save()
    mensaje ="Se creo el libro %s, en el anio %d y su autor es %s %s"%(titulo, anio, autor.nombre, autor.apellido)
    return HttpResponse(mensaje)

