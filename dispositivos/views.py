from django.shortcuts import render
from django.http import HttpResponse
from .services import cargar_dispositivos,cargar_zonas


def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(
        request,
        "dispositivos/inicio.html",
        contexto,
    )

def dispositivos_zona(request,zona_id):
    if zona_id != 3:
        return HttpResponse(
            "Zona no encontrada", status=404
        )
    return HttpResponse(
        f"Dispositivos de la zona {zona_id}"
    )

def ubicacion_zona(request,zona_id):
    if zona_id != "claves":
        return HttpResponse(
            "Bien ahi", status=404
        )
    return HttpResponse(
        f"Que buscas Hacker???")

def catalogo(request):
    dispositivos = cargar_dispositivos()
    
    contexto = {
        "dispositivos": dispositivos,
        "total": len(dispositivos),
        
    }
    return render(
        request, "dispositivos/catalogo.html", contexto
    )

def zonascatalogo(request):
    zonas = cargar_zonas()
    dispositivos = cargar_dispositivos()

    for zona in zonas:
        zona["dispositivos"] = [
            d for d in dispositivos if d["zona_id"] == zona["id"]
        ]

    contexto = {
        "zonas": zonas,
        "total": len(zonas),
    }
    return render(
        request, "dispositivos/zonas.html", contexto
    )

def info(request):
    informacion = {
        "texto": "Somos una empresa comprometida con la energia.",
        "direccion": "Av. Aguirre #242",
    }
    return render(
        request,
        "dispositivos/info.html",
        informacion,
    )