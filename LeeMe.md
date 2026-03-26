# Proyecto Espais — Bitácora y pasos

---

## Estado actual del proyecto

### 1️⃣ Crear archivo de dependencias

```bash
pip freeze > requirements.txt
```

---

## Recursos

* Flask
* Bootstrap: [https://getbootstrap.com/](https://getbootstrap.com/)
* FontAwesome: [https://fontawesome.com/](https://fontawesome.com/)

---

## Archivos principales

* Archivo principal: `run.py`
* Configuración: `config.py`

---

## Estructura base del proyecto

```
Proyecto/
│
├── run.py
├── config.py
├── requirements.txt
│
└── main/
    ├── __init__.py
    ├── auth.py
    ├── espacio.py
    ├── home.py
    ├── models.py
    │
    ├── templates/
    │   ├── base.html
    │   ├── blog.html
    │   ├── index.html
    │   ├── admin/
    │   │   ├── create.html
    │   │   ├── post.html
    │   │   └── update.html
    │   └── auth/
    │       ├── login.html
    │       ├── profile.html
    │       └── register.html
    │
    └── static/
        ├── css/
        │   ├── all.min.css
        │   ├── bootstrap.min.css
        │   ├── login.css
        │   └── style.css
        ├── img/
        └── js/
            └── bootstrap.bundle.min.js
```

---

## Descripción de módulos

* `auth.py`     → Controlador de vistas y rutas de autenticación
* `espacio.py`  → Gestión de publicaciones / espacios
* `home.py`     → Página principal o de inicio
* `models.py`   → Modelos de base de datos

---

# Documento organizado copia de seguridad del estado del proyecto

---

## 1 — Creamos vistas y rutas con Blueprint en los archivos

Se registran y organizan los Blueprints:

* home
* auth
* espacio

---

## 2 — Organización de templates y estáticos

### Templates

* base.html
* blog.html
* index.html
* admin/

  * create.html
  * post.html
  * update.html
* auth/

  * login.html
  * profile.html
  * register.html

### Static

* css/

  * all.min.css
  * bootstrap.min.css
  * login.css
  * style.css
* img/
* js/

  * bootstrap.bundle.min.js

---
## 3 — Uniendo Frontend con Flask
### Unimos y creamos base.html y vamos agregando los archivos css necesarios y dando las rutas correctas.
 * `<link rel="stylesheet" href="{{ url_for('static', filename = 'css/style.css') }}">`
 * `<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap" rel="stylesheet">`
 * `<script src="{{ url_for('static', filename = 'js/bootstrap.bundle.min.js') }}"></script>`
 * Imagenes `<img src="{{ url_for('static', filename = 'img/bp-light.png') }}" alt="blog posts" width="40">`
 ## Cargaremos diferentes CSS segun la paguina. En este caso login o registrarse... etc.

 ---
 ## 4 — Configurando Config.py
 ## Para instalar las conexiones a las bases de datos necesitaremos:
   * pip install flask-sqlalchemy
   * pip install psycopg2     
### Desde init cargamos el archivo de configuracion.
  * Realizamos la conexión a la BD
  * Iniciamos la BD en nuestor fichero init
  * Creamos las tablas que le daremos forma en models.py

 ## 5 — Autentificación de usuarios:
  * Preparamos la plantilla register.html
  * Preparamos la plantilla login
  * Trabajamos en el modulo auth.py el codigo python.
    * Configuramos el codigo para recibir los datas de la plantilla e inviarlo a la base de datos.  
    * Configuramos los mensajes de error de la aplicación.

## Menus de navegació
  * 
  

# Commits y modificaciones.
##  26/03/2026
### Initial commit - estructura base Flask espais
### Actualizar gitignore y añadir Git.md
### Se oculta el boton de registrarse que esta en base.html
