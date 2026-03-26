# auth.py

from flask import Blueprint, render_template, request, url_for, redirect,flash,session, g

from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from main import db

# - Creamos el Blueprint de autenticación con prefijo /auth
bp = Blueprint('auth', __name__, url_prefix='/auth')

# - Define la ruta /auth/register y permite mostrar el formulario (GET) y procesarlo (POST)
@bp.route('/register', methods = ('GET', 'POST'))                             
def register():                                          # - Vista para la página de registro de usuarios
    
    if request.method == 'POST':
        username    = request.form.get('username')      # - Obtiene el nombre de usuario del formulario
        email       = request.form.get('email')         # - Obtiene el email del usuario
        password    = request.form.get('password')      # - Obtiene la contraseña en texto plano   
        
        user = User(username, email, generate_password_hash(password))          
        
        # !Validación de datos
        error = None
        # -Comparando nombre de usuario con los existentes
        user_email = User.query.filter_by(email = email).first()
        # -Condición si NO existe
        if user_email == None:
            db.session.add(user)
            db.session.commit()
        
            return redirect(url_for('auth.login'))
        else:
            error = f'Atenció, el correo {email} ja està registrat'
        flash(error)    
    return render_template('auth/register.html')                            # - Respuesta temporal en texto plano

# - Ruta: /auth/login ---------------------CARGAMOS LOGIN ------------------------------------------------------
@bp.route('/login', methods = ('GET', 'POST'))                                 
def login():                                        # - Vista para la página de inicio de sesión
    
    if request.method == 'POST':
        email = request.form.get('email')          # - Obtiene el email de usuario del formulario
        password = request.form.get('password')    # - Obtiene el password del usuario

        # **Validación de datos
        error =None
        # **Comparando nombre de usuario con los existentes
        user = User.query.filter_by(email = email).first()
        
        # **Si no existe o es mala la pas
        if user == None or not check_password_hash(user.password, password):
            error = 'Email o password incorrecta'
            
        # **Iniciar SESIÓN**
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('post.posts'))    
        flash(error)    
    return render_template('auth/login.html')       # - Respuesta temporal en texto plano

#..........................................................................................................
# -Mantener el inicio de SESIÓN CARGADA CON LOGOUT i un decorador que pida a las demas vistas que se inicie sesión

@bp.before_app_request                                  # -Esta función se ejecuta **antes de cada petición** a la aplicación.
def load_logged_in_user():                              # -Se utiliza para cargar automáticamente el usuario que haya iniciado sesión.
    user_id = session.get('user_id')                    # -Recupera el ID del usuario almacenado en la sesión

    if user_id is None:
        g.user = None                                   # -Si no hay usuario en sesión, g.user se establece como None
    else:
        g.user = User.query.get_or_404(user_id)         # -Si hay usuario, carga el objeto User desde la base de datos
                                                        # -Si no lo encuentra, lanza un error 404
                                                        
# -CIERRA TODA LA SESIÓN DEL USUSARIO.                                                      
@bp.route('/logout')                                                        
def logout():                                           
    session.clear()
    return redirect(url_for('home.index'))              # -Redirige al usuario a la ruta 'index'
                                                        # -(normalmente la página de inicio o login)
                                                        
import functools                                        # !Decorador para exigir login

def login_required(view):                               # - Define el decorador que exige que el usuario esté logueado
    @functools.wraps(view)                              # - Mantiene el nombre y metadatos originales de la función decorada
    def wrapped_view(**kwargs):                         # - Envuelve la vista original para comprobar si el usuario está autenticado
        if g.user is None:                              # - Si no hay usuario cargado, significa que no ha iniciado sesión
            return redirect(url_for('auth.login'))      # - Redirige al formulario de login
        return view(**kwargs)                           # - Si hay usuario autenticado, ejecuta la vista original
    return wrapped_view                                 # - Devuelve la función decorada


# -FUNCIÓN PARA CARGAR FOTO - Editar Perfil oadministrar perfil.
# .Limpia y asegura nombres de archivos para evitar rutas peligrosas al subir ficheros
from werkzeug.utils import secure_filename

def get_photo(id):
    user = User.query.get_or_404(id)
    photo =None
    if photo != None:
        photo = user.photo
    return photo
    
    

# - Ruta de perfil de usuario editar perfil
@bp.route('/profile/<int:id>', methods = ('GET', 'POST'))
@login_required
def profile(id):
    user = User.query.get_or_404(id)
    
    
    if request.method == 'POST':
        user.username = request.form.get('username')        # - Obtiene el nombre de usuario del formulario
        
        password = request.form.get('password')             # - Obtiene la contraseña en texto plano
        
        error = None
        if len(password) != 0:
            user.password = generate_password_hash(password)
        elif len(password) > 0 and len(password) < 4 :
            error = 'La constraseña deve tener más de 3 caracteres'
        
        if request.files['photo']:                                                  # - Comprueba si se ha enviado un archivo de foto
            photo = request.files['photo']                                          # - Obtiene el archivo de la foto
            photo.save(f'main/static/media/{secure_filename(photo.filename)}')     # - Guarda la foto en /static/media
            user.photo = f'media/{secure_filename(photo.filename)}'                 # - Guarda la ruta de la foto en BD
            
        if error is not None:                                       # - Si hay error, se muestra mensaje
            flash(error)
        else:
            db.session.commit()                                     # - Guarda los cambios en la base de datos
            return redirect(url_for('auth.profile', id=user.id))    # - Redirige al perfil actualizado
        flash(error)                                                # - Muestra el error en pantalla
    
    
    return render_template('auth/profile.html', user = user)


