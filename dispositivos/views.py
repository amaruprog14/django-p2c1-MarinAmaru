from django.shortcuts import render
from django.http import HttpResponse, Http404
from .services import cargar_dispositivos,cargar_zonas,cargar_categorias

# Muestra la página de inicio con la informacion general del sistema
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

# Vista de prueba
def dispositivos_zona(request,zona_id):
    if zona_id != 3:
        return HttpResponse(
            "Zona no encontrada", status=404
        )
    return HttpResponse(
        f"Dispositivos de la zona {zona_id}"
    )

# Vista de prueba
def ubicacion_zona(request,zona_id):
    if zona_id != "claves":
        return HttpResponse(
            "Bien ahi", status=404
        )
    return HttpResponse(
        f"Que buscas Hacker???")

# Muestra el catalogo completo de dispositivos
def catalogo(request):
    dispositivos = cargar_dispositivos()
    
    contexto = {
        "dispositivos": dispositivos,
        "total": len(dispositivos),
        
    }
    return render(
        request, "dispositivos/catalogo.html", contexto
    )

# Muestra el listado de zonas, cada una con sus dispositivos asociados
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

# Muestra la pagina de informacion de la empresa
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

# Muestra el detalle de una zona, sus dispositivos, consumo total y estado
def detalle_zona(request, zona_id):
    lista_zonas = cargar_zonas()

    zona = None
    for zona_actual in lista_zonas:
        if zona_actual["id"] == zona_id:
            zona = zona_actual
            break

    if zona is None:
        raise Http404("Zona no encontrada")

    lista_dispositivos = cargar_dispositivos()
    lista_categorias = cargar_categorias()

    dispositivos_de_la_zona = [
        dispositivo
        for dispositivo in lista_dispositivos
        if dispositivo["zona_id"] == zona_id
    ]

    for dispositivo in dispositivos_de_la_zona:
        categoria = None
        for categoria_actual in lista_categorias:
            if categoria_actual["id"] == dispositivo["categoria_id"]:
                categoria = categoria_actual
                break
        dispositivo["categoria_nombre"] = categoria["nombre"] if categoria else "Sin categoría"

    consumo_total = sum(dispositivo["consumo_kwh"] for dispositivo in dispositivos_de_la_zona)
    estado = "ALERTA" if consumo_total > zona["limite_kwh"] else "NORMAL"

    contexto = {
        "zona": zona,
        "dispositivos": dispositivos_de_la_zona,
        "consumo_total": consumo_total,
        "estado": estado,
    }
    return render(request, "dispositivos/detalle_zona.html", contexto)

def resumen_zonas(request):
    zonas = cargar_zonas()
    dispositivos = cargar_dispositivos()

    for zona in zonas:
        zona["dispositivos"] = [
            d for d in dispositivos if d["zona_id"] == zona["id"]
        ]
    dispositivos_de_la_zona = [
        dispositivo
        for dispositivo in dispositivos
        if dispositivo["zona_id"] == zona["id"]
    ]
    
    
    consumo_total = sum(dispositivo["consumo_kwh"] for dispositivo in dispositivos)
    estado = "LIMITE SUPERADO" if consumo_total > zona["limite_kwh"] else "DENTRO DEL LIMITE"
    # consumo_zona =

    contexto = {
        "zonas": zonas,
        "dispositivos": dispositivos,
        "total": len(zonas),
        "total_dispositivos":len(dispositivos),
        "consumo_total": consumo_total,
        "estado": estado
    }
    return render(
        request, "dispositivos/resumen_zonas.html", contexto
    )