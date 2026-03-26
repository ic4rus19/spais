# models.py

from main import db
from datetime import datetime

# - Modelo de Usuario
class User(db.Model):
    __tablename__ = 'users'
    
    # - Campos principales del usuario
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(255))
    
    # - Constructor del modelo
    def __init__(self, username, email, password, photo=None):
        self.username = username
        self.email = email
        self.password = password
        self.photo = photo
    
    # - Representacion en consola
    def __repr__(self):
        return f"User: '{self.username}'"


# - Modelo de Espais
class Post(db.Model):
    __tablename__ = 'espacios'
    
    # - Campos base
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    url = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    
    # - Dades principals
    edifici = db.Column(db.String(150))
    tipus_espai = db.Column(db.String(150))
    adreca = db.Column(db.String(255))
    horaris = db.Column(db.String(255))
    
    # - Capacitat i control
    superficie_m2 = db.Column(db.String(50))
    aforament_maxim = db.Column(db.String(50))
    estat_conservacio = db.Column(db.String(100))
    claus = db.Column(db.String(100))
    neteja = db.Column(db.String(100))
    
    # - Gestio
    sistema_reserva = db.Column(db.String(255))
    responsable_municipal = db.Column(db.String(150))
    telefon = db.Column(db.String(50))
    email = db.Column(db.String(120))
    taxa_preu_public = db.Column(db.String(100))
    
    # - Descripcio i contingut
    info = db.Column(db.Text)
    observacions = db.Column(db.Text)
    content = db.Column(db.Text)
    
    # - Data de creacio
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # - Constructor del modelo
    def __init__(
        self,
        author,
        url,
        title,
        info,
        content,
        edifici=None,
        tipus_espai=None,
        adreca=None,
        horaris=None,
        superficie_m2=None,
        aforament_maxim=None,
        estat_conservacio=None,
        claus=None,
        neteja=None,
        sistema_reserva=None,
        responsable_municipal=None,
        telefon=None,
        email=None,
        taxa_preu_public=None,
        observacions=None
    ) -> None:
        self.author = author
        self.url = url
        self.title = title
        self.info = info
        self.content = content
        self.edifici = edifici
        self.tipus_espai = tipus_espai
        self.adreca = adreca
        self.horaris = horaris
        self.superficie_m2 = superficie_m2
        self.aforament_maxim = aforament_maxim
        self.estat_conservacio = estat_conservacio
        self.claus = claus
        self.neteja = neteja
        self.sistema_reserva = sistema_reserva
        self.responsable_municipal = responsable_municipal
        self.telefon = telefon
        self.email = email
        self.taxa_preu_public = taxa_preu_public
        self.observacions = observacions
            
    # - Representacion en consola
    def __repr__(self) -> str:
        return f"Post: {self.title}"