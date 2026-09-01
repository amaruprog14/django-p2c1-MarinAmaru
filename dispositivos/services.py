import json
from django.conf import settings
from django.shortcuts import render

def cargar_dispositivos():
    ruta = settings.BASE_DIR / "data" / "dispositivos.json"
    
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    
    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de dispositivos")
    return datos

def cargar_zonas():
    ruta = settings.BASE_DIR / "data" / "zonas.json"
    
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    
    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de zonas")
    return datos

def zonas(request):
    zonas_data = cargar_zonas()
    dispositivos_data = cargar_dispositivos()
 
    for zona in zonas_data:
        zona["dispositivos"] = [
            d for d in dispositivos_data if d["zona_id"] == zona["id"]
        ]
    return render(request, "zonas.html", {"zonas": zonas_data})