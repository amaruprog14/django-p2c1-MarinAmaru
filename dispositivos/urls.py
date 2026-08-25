from django.urls import path
from . import views

app_name = "dispositivos"

urlpatterns = [
    path("",views.inicio,name="inicio"),
    path(
        "zonas/<int:zona_id>/dispositivos/",
        views.dispositivos_zona,
        name="por_zona",
    ),
    path(
        "zonas/<str:zona_id>/dispositivos/",
        views.ubicacion_zona,
        name="por_zona_ubicacion",
    ),
    path("dispositivos/", views.catalogo, name="catalogo"),
    path("info/", views.info, name="info")
]