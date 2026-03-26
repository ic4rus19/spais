# config.py
# -Separamos nuestra aplicacion mediante este archivo



# - Creamos una clase que contendra toda la configuración
# - Agregaremos variables que tengan la configuración de nuestro proyecto

SQLITE = "sqlite:///project.db"
POSTGRESQL = "postgresql+psycopg2://postgres:Colorado1-@localhost:5432/espais"


class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    
    SQLALCHEMY_DATABASE_URI = POSTGRESQL
    
    CKEDITOR_PKG_TYPE = 'full'


