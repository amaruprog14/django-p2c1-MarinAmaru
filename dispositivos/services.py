import json
from django.conf import settings
from django.shortcuts import render

# Lee dispositivos.json y devuelve la lista de dispositivos registrados
def cargar_dispositivos():
    ruta = settings.BASE_DIR / "data" / "dispositivos.json"
    
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    
    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de dispositivos")
    return datos

# Lee zonas.json y devuelve la lista de zonas registradas
def cargar_zonas():
    ruta = settings.BASE_DIR / "data" / "zonas.json"
    
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    
    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de zonas")
    return datos

# Muestra el listado de zonas, cada una con sus dispositivos asociados
def zonas(request):
    lista_zonas = cargar_zonas()
    lista_dispositivos = cargar_dispositivos()

    for zona in lista_zonas:
        dispositivos_de_la_zona = [
            dispositivo
            for dispositivo in lista_dispositivos
            if dispositivo["zona_id"] == zona["id"]
        ]
        zona["dispositivos"] = dispositivos_de_la_zona

    return render(request, "zonas.html", {"zonas": lista_zonas})

# Lee categorias.json y devuelve la lista de categorias registradas
def cargar_categorias():
    ruta = settings.BASE_DIR / "data" / "categorias.json"

    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)

    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de categorias")
    return datos