# 🐍 PYTHON 3.12.8 — DOCUMENTO MAESTRO (Enfoque Git).

Guía centrada en:
- Git local
- Git en PythonAnywhere
- Flujo de actualización
- Despliegue
- Entorno y estructura Flask

---

# 1️⃣ CONTROL DE VERSIONES — GIT (LOCAL)

## Crear archivo de dependencias

```bash
pip freeze > requirements.txt
```

---

## Flujo básico diario

```bash
git status              # Ver estado actual
git log --oneline       # Ver historial resumido
git add .
git commit -m "Mensaje"
git push
```

---

## Ver historial completo

```bash
git log
git log --oneline
git log --oneline --graph --decorate --all
```
---
## Actualizar desde remoto PCAnywere

```bash
git fetch   # Trae información (no modifica archivos)
git pull    # Descarga y aplica cambios
```
Comprobación:

```bash
git log -1 --oneline
```
---
# 2️⃣ GIT EN PYTHONANYWHERE (SERVIDOR)

## Primera vez
```bash
git clone https://github.com/usuario/proyecto.git
```

#  ENTORNO LOCAL

## Crear entorno virtual

```bash
mkdir nProyecto
cd nProyecto
python -m venv env
.\env\Scripts\activate
python -m pip install --upgrade pip
pip install flask
pip list
deactivate
```

---

## Dependencias adicionales

### Formularios
```bash
pip install -U Flask-WTF
pip install flask-ckeditor
```

### Base de datos
```bash
pip install Flask-SQLAlchemy
pip install psycopg2
```

---

# 4️⃣ DESPLIEGUE EN PYTHONANYWHERE

## Crear nueva Web App

WEB → Add a new web app → Flask → Seleccionar versión.

Revisar:
- Code
- wsgi.py
- Consola Linux

---

## Crear entorno virtual en servidor

```bash
python --version
git --version
mkvirtualenv --python=python3.13 .NombreEntorno
```

Instalar dependencias:

```bash
pip install -r requirements.txt
pip list
```

---

## Configurar wsgi.py

```python
import sys

project_home = '/home/usuario/NOMBRE_PROYECTO'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from run import app as application
```

Reload desde Web.

---
# 5️⃣ ESTRUCTURA PROFESIONAL FLASK

```
run.py
config.py

blogr/
│
├── __init__.py
├── templates/
├── static/
├── auth.py
├── post.py
├── home.py
└── models.py
```

---

# 6️⃣ CONCEPTOS CLAVE

## Endpoints

- Flask enruta por endpoints, no por archivos
- `url_for()` usa endpoints
- Con Blueprints → `blueprint.funcion`

---

## Métodos HTTP

**GET**
- Mostrar páginas
- No modifica datos

**POST**
- Crear o modificar información
- No envía datos en la URL

---

# 🚀 INICIAR APLICACIÓN

```bash
python run.py
```

---

# 📌 RESUMEN

Documento enfocado en:

✔ Git local  
✔ Git servidor  
✔ Actualizaciones seguras  
✔ Despliegue PythonAnywhere  
✔ Estructura Flask  
✔ Dependencias  
✔ PostgreSQL  

Base operativa para cualquier proyecto Flask.



# 📝 ANEXO — Notas destacadas

## 📁 Carpeta instance (Base de datos)

Se creará la carpeta `instance/` donde se alojará la base de datos.  
Podemos cambiar el nombre del archivo `.db` si es necesario.

Esto permite que Flask gestione correctamente la conexión a la base de datos.  
(Referencia: Lección 36)

---

## 🌐 Dominio en PythonAnywhere

El dominio de pruebas tendrá el nombre del usuario:

```
usuario.pythonanywhere.com
```

Ejemplo:
```
ic4rus.pythonanywhere.com
```

---

## 🔄 Rehacer despliegue en PythonAnywhere

Si es necesario reiniciar desde cero:

- Borrar aplicación anterior.
- Crear nueva Web App.
- Configurar manualmente.
- Revisar `wsgi.py`.
- Hacer Reload desde Web.

---

## 🧠 Recordatorio importante

En el servidor:

- Crear entorno virtual antes de instalar dependencias.
- Clonar proyecto después de crear el entorno.
- Instalar dependencias desde `requirements.txt`.

Orden correcto:
```bash
mkvirtualenv --python=python3.13 .NombreEntorno
git clone https://github.com/usuario/proyecto.git
pip install -r requirements.txt
```

---

## 🗄 PostgreSQL — Librerías necesarias

Instalar librerías:

```bash
pip install flask-sqlalchemy
pip install psycopg2
```

### ¿Qué aporta cada una?

- **flask-sqlalchemy**
  - Integra SQLAlchemy con Flask.
  - Permite definir modelos como clases.
  - Gestiona la conexión a la base de datos.
  - Facilita consultas ORM (sin escribir SQL directamente).

- **psycopg2**
  - Es el conector oficial de Python para PostgreSQL.
  - Permite que SQLAlchemy se comunique con la base de datos PostgreSQL.

---

Cadena de conexión ejemplo:

```
postgresql://usuario:password@localhost/nombrebd
```

Formato:
```
postgresql://USUARIO:CONTRASEÑA@HOST/NOMBRE_BASE_DATOS
```

## 🧪 Usuario de prueba (Proyecto Espacios Públicos)

Usuario ejemplo utilizado en pruebas:

```
mabel@gmail
1234
```

---

## ⚠ Recordatorio de clase

Revisar especialmente:
- Configuración de la base de datos.
- Uso correcto de endpoints.
- Separación por Blueprints.