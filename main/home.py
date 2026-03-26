# home.py

from flask import Blueprint, render_template, request
from .models import User, Post

bp = Blueprint('home', __name__)

# -Función con la que obtendremos al usuario para el index y mostrar su blog
def get_user(id):
    user = User.query.get_or_404(id)
    return user

# -Mostrar todos los POST
@bp.route('/', methods=['GET', 'POST'])        # - Ruta principal de la aplicación o BASE
def index():                                    # - Vista que gestiona la página de inicio
    posts = Post.query.all()
    
    if request.method == 'POST':
        query = request.form.get('search')
        posts = search_post(query)
        value = 'hidden'
        return render_template('index.html', posts = posts, get_user= get_user, value=value)    
    return render_template('index.html', posts = posts, get_user = get_user)

# -BUSQUEDAS
def search_post(query):
    posts = Post.query.filter(Post.title.ilike(f'%{query}%')).all()
    return posts


# -Busquedas que mostraremos mediante el URL
@bp.route('/blog/<url>')
def blog(url):  
    
    post = Post.query.filter_by(url= url).first()
    
    return render_template('blog.html', post=post, get_user = get_user)