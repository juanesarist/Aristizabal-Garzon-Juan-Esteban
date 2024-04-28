from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):

    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<h1> Segunda vista </h1>")

def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")

def probando_template(request):
    nombre = "Juan"
    apellido = "Aristizabal"
    datos = {"nombre": nombre, "apellido": apellido}
    return render(request, "template1.html", context = datos)

def probando_template2(request):
    lista_de_notas = [5, 8, 6, 7, 10, 9, 7, 3, 3, 4, 1]
    datos_notas = {"notas": lista_de_notas}
    return render(request, "template2.html", context = datos_notas)