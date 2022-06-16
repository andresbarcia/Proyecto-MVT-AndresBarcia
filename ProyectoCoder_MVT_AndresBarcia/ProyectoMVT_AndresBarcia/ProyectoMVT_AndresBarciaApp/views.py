from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.template import Template, Context
from scipy.fftpack import ss_diff

# Create your views here.

def inicio(request):

    mi_familia = "Mi papá se llama: Eduardo, mi mamá se llama: Fabiana y tengo dos hermanos: Mathias y Abril"
    #mi_familia = (nombres)
    fecha_hora = datetime.datetime.now()
    #edades_familia = (edades)
    edades_familia = "Mi padre tiene: 49, mamá tiene: 46 y mis hermanos tienen: 25 y 16 respectivamente."

    #with open(r"C:\Users\andre\Desktop\Curso Python -- CODER HOUSE\Scripts del curso\ProyectoCoder_MVT_AndresBarcia\ProyectoMVT_AndresBarcia\ProyectoMVT_AndresBarciaApp\Templates\index.Html") as file:
        #plantillabase = Template(file.read())
    
    #contextobase = Context({ "familia" : mi_familia, "fecha_a" : fecha_hora, "edades" : edades_familia })

    return render(request,"index.Html",{ "familia" : mi_familia, "fecha_a" : fecha_hora, "edades" : edades_familia })

def saludo(request):

    saludo = "Saludos desde nuestra familia!"
    
    return HttpResponse (saludo)

def nombres(request):
    
    familia = {{'Padre' : "Eduardo", 'Madre': "Fabiana", 'HermanoMenor' : "Mathias", 'HermanaMenor' : "Abril"}}

    return HttpResponse (f"Los integrantes de mi familia son: ", familia)

def edades(request):

    edades_familia = {{'Eduardo': 49, 'fabiana': 46, 'Mathias': 25, 'Abril': 16}}

    return HttpResponse("Ultima actualización: ", edades_familia)


def tiempo(request):

    fecha_hora = datetime.datetime.now()

    return HttpResponse("Ultima actualización: ", fecha_hora)
