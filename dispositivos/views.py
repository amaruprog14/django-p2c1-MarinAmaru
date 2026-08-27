from django.shortcuts import render
from django.http import HttpResponse
from .services import cargar_dispositivos, cargar_consumos


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
    activos = sum(
        1 for item in dispositivos
        if item["estado"] == "Activo"
    )
    contexto = {
        "dispositivos": dispositivos,
        "total": len(dispositivos),
        "total_activos": activos,
    }
    return render(
        request, "dispositivos/catalogo.html", contexto
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