#A cada función creada dentro del archivo views, se le denomina vista

from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona():

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



#Primera vista
def saludo(request):

    p1 = Persona("Jermaine","Cole")  

    nombre = "Julio"
    apellido = "Díaz"

    ahora=datetime.datetime.now()

    #doc_externo = open("C:/Users/Julio C/Documents/Django/proyecto1Django/Proyecto1/Proyecto1/plantillas/plantilla1.html")

    #plt = Template(doc_externo.read())

    #doc_externo.close()

    doc_externo = loader.get_template('plantilla1.html')

    #Creamos el contexto
    #ctx = Context({"nombre_persona":nombre,"apellido_persona":apellido,"nombre_alumno":"Julio Bernal","momento_actual":ahora,"nombre_poeta":p1.nombre,"apellido_poeta":p1.apellido})

    #Renderizamos
    documento = doc_externo.render({"nombre_persona":nombre,"apellido_persona":apellido,"nombre_alumno":"Julio Bernal","momento_actual":ahora,"nombre_poeta":p1.nombre,"apellido_poeta":p1.apellido})

    return HttpResponse(documento)


#Segunda vista
def despedida(request):

    documento = """<html>
    <body>
    <h1>
    Arriba las chivas
    </html></body>
    </h1>"""
    return HttpResponse(documento)

#Tercer vista
def encuesta1(request):
    return HttpResponse("\tBienvenido a la encuesta")

#Cuarta vista
def damefecha(request):

    fecha_actual=datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales: %s
    </html></body>
    </h2>""" % fecha_actual
    return HttpResponse(documento)

#Quinta vista
def calculaedad(request,edad,agno): 
    #edadActual = 18
    periodo = agno-2020
    edadFutura = edad+periodo
    documento = f"<html><body><h2> En el año {agno} tendras {edadFutura}"

    return HttpResponse(documento)


# Sexta vista
def pruebamenu(request):

    temasDelCurso = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    
    archivo = open("C:/Users/Julio C/Documents/Django/proyecto1Django/Proyecto1/Proyecto1/plantillas/plantilla2.html")
    
    plantilla = Template(archivo.read())

    archivo.close()

    ctx = Context({"temas":temasDelCurso})

    documento = plantilla.render(ctx)

    return HttpResponse(documento)


#Séptima vista

def calendario(request):

    jugador1 = Persona("Julio","Bernal")
    listaavatares = ["Superman","Batman","Guasón","Iron Man"]

    plantilla = loader.get_template('plantilla3.html')

    documento = plantilla.render({"nj1":jugador1.nombre, "aj1":jugador1.apellido, "lista":listaavatares})
    
    return HttpResponse(documento) 


def goku(request):

    jugador2 = Persona("Herman","Hesse")
    lista = [i for i in range(1,11)]

    diccionario = {"nj2":jugador2.nombre,"aj2":jugador2.apellido,"numeros":lista}

    return render(request,'plantilla4.html',diccionario)

def reason(request):

    fecha_actual=datetime.datetime.now()

    return render(request,'cursoC.html', {"dameFecha":fecha_actual})

def jcole(request):

    fecha_actual=datetime.datetime.now()

    return render(request,'jcole.html', {"dameFecha":fecha_actual})
