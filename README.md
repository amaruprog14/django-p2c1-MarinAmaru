# EcoEnergy - Backend

## Descripción y objetivo
EcoEnergy es una aplicación web para administrar dispositivos y monitorear su consumo energético en hogares o empresas. 
El objetivo de este proyecto es construir un backend que permita gestionar usuarios, autenticación, zonas y dispositivos, además de registrar y enviar alertas de consumo mediante una API REST.

## Requisitos previos
Para ejecutar este proyecto, asegúrate de tener instalado:
* Python
* Git
* Una terminal compatible (Git Bash o PowerShell)

## Clonación del repositorio
Abre tu terminal y ejecuta los siguientes comandos para obtener una copia local del proyecto:
```bash
git clone https://github.com/amaruprog14/django-p2c1-MarinAmaru.git
cd django-p2c1-MarinAmaru.git
```

## Creación y activación de .venv
Es fundamental utilizar un entorno virtual aislado para no afectar la configuración global de tu sistema.

1. Crea el entorno virtual:
```bash
python -m venv .venv
```

2. Actívalo según la terminal que estés utilizando:
* **En Git Bash:**
  ```bash
  source .venv/Scripts/activate
  ```
* **En PowerShell:**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  *(Si PowerShell bloquea la ejecución, utiliza: `Set-ExecutionPolicy ExecutionPolicy RemoteSigned -Scope Process`)*

## Comandos de verificación
Antes de continuar, verifica que estás ejecutando Python desde tu entorno virtual y no desde el sistema global:
```bash
python -c "import sys; print(sys.executable)"
```
El resultado debe mostrar la ruta interna de tu proyecto (por ejemplo, `...\.venv\Scripts\python.exe`).

## Instalación desde requirements.txt
Una vez verificado y activado el entorno, instala las dependencias necesarias (como Django) usando el archivo de registro:
```bash
python -m pip install -r requirements.txt
```

## Ejecución y comprobación del proyecto

Para comprobar que la base del proyecto funciona sin errores y levantar el servidor:
```bash
python manage.py check
python manage.py runserver
```
Puedes abrir tu navegador en `http://127.0.0.1:8000` para ver la página inicial.

## Estado actual
* **Estado actual:** Proyecto base de Django configurado de manera reproducible, con entorno virtual aislado y dependencias documentadas.
