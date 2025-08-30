# Library Inventory App

By:
- Luis Ruben Ramos Cortes
- Ruben Jimenez Navarro


# Instrucciones de ejecucion

> ⚠️ **Antes de comenzar asegurate de tener Python 3 y pip instalados**

## 1. Clonar el repositorio de github

```
git clone https://github.com/kekewicho/library-inventory-app.git
cd library-inventory-app
```


## 2. Inicialización de base de datos
Como el proyecto utiliza SQLite por defecto, no necesitas configurar un servidor de base de datos. Sin embargo, debes ejecutar las migraciones para crear las tablas de los modelos Autor y Libro.


```
python manage.py makemigrations
python manage.py migrate
```


## 3. Inicia el servidor

```
python manage.py runserver
```


## 4. Accede a la aplicacion desde tu navegador

Accede a la ruta [/inventory](http://localhost:8000/inventory)



# Funcionamiento

[IMG1](static\evidencia\Captura de pantalla 2025-08-30 145647.png)
