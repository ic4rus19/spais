# ! post.py

from flask import Blueprint, render_template, request, flash, redirect, url_for, g

from .auth import login_required
from .models import Post

from main import db

# - Blueprint de gestion de posts
bp = Blueprint('post', __name__, url_prefix='/post')


# - Listado de posts del sistema
@bp.route('/posts')
@login_required
def posts():
    posts = Post.query.all()                                   # - Consulta todos los posts
    return render_template('admin/posts.html', posts=posts)    # - Renderiza la tabla


# - Creamos ESPAI
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        # - Dades principals
        url = request.form.get('url')
        url = url.replace(' ', '-')
        title = request.form.get('title')
        edifici = request.form.get('edifici')
        tipus_espai = request.form.get('tipus_espai')
        adreca = request.form.get('adreca')
        horaris = request.form.get('horaris')

        # - Capacitat i control
        superficie_m2 = request.form.get('superficie_m2')
        aforament_maxim = request.form.get('aforament_maxim')
        estat_conservacio = request.form.get('estat_conservacio')
        claus = request.form.get('claus')
        neteja = request.form.get('neteja')

        # - Gestio
        sistema_reserva = request.form.get('sistema_reserva')
        responsable_municipal = request.form.get('responsable_municipal')
        telefon = request.form.get('telefon')
        email = request.form.get('email')
        taxa_preu_public = request.form.get('taxa_preu_public')

        # - Descripcio i contingut
        info = request.form.get('info')
        observacions = request.form.get('observacions')
        content = request.form.get('content')

        error = None

        # - Comprovem si la url ja existeix
        post_url = Post.query.filter_by(url=url).first()

        if post_url is None:
            post = Post(
                g.user.id,
                url,
                title,
                info,
                content,
                edifici,
                tipus_espai,
                adreca,
                horaris,
                superficie_m2,
                aforament_maxim,
                estat_conservacio,
                claus,
                neteja,
                sistema_reserva,
                responsable_municipal,
                telefon,
                email,
                taxa_preu_public,
                observacions
            )

            db.session.add(post)
            db.session.commit()

            flash(f"L’espai {post.title} s’ha registrat correctament")
            return redirect(url_for('post.posts'))
        else:
            error = f"L’espai {url} ja està registrat"

        flash(error)

    return render_template('admin/create.html')


# - Editar o modificar un espai
@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    post = Post.query.get_or_404(id)

    if request.method == 'POST':
        # - Dades principals
        post.title = request.form.get('title')
        post.edifici = request.form.get('edifici')
        post.tipus_espai = request.form.get('tipus_espai')
        post.adreca = request.form.get('adreca')
        post.horaris = request.form.get('horaris')

        # - Capacitat i control
        post.superficie_m2 = request.form.get('superficie_m2')
        post.aforament_maxim = request.form.get('aforament_maxim')
        post.estat_conservacio = request.form.get('estat_conservacio')
        post.claus = request.form.get('claus')
        post.neteja = request.form.get('neteja')

        # - Gestio
        post.sistema_reserva = request.form.get('sistema_reserva')
        post.responsable_municipal = request.form.get('responsable_municipal')
        post.telefon = request.form.get('telefon')
        post.email = request.form.get('email')
        post.taxa_preu_public = request.form.get('taxa_preu_public')

        # - Descripcio i contingut
        post.info = request.form.get('info')
        post.observacions = request.form.get('observacions')
        post.content = request.form.get('content')

        db.session.commit()
        flash(f'Espai {post.title} actualitzat correctament')
        return redirect(url_for('post.posts'))

    return render_template('admin/update.html', post=post)


# - Eliminar espai
@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    flash(f'Espai {post.title} eliminat correctament')

    return redirect(url_for('post.posts'))