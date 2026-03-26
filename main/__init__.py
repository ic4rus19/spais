# __init__.py


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# - Inicializamos la extension de base de datos
db = SQLAlchemy()

def create_app():
    # - Creamos la aplicacion
    app = Flask(__name__)
    
    # -IDIOMAS

    import locale
    locale.setlocale(locale.LC_ALL, 'es_ES')
    
    # - Cargamos la configuracion
    app.config.from_object('config.Config')
    
    # - Vinculamos la base de datos
    db.init_app(app)
    
    # - Registramos los blueprints
    from main import home
    app.register_blueprint(home.bp)
    
    from main import auth
    app.register_blueprint(auth.bp)
    
    from main import post
    app.register_blueprint(post.bp)
    
    # - Importamos los modelos
    from .models import User, Post
    
    # - Creamos las tablas si no existen
    with app.app_context():
        db.create_all()
    
    # - Retornamos la aplicacion
    return app