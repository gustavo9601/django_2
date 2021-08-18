from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from typing import List

from posts.forms import PostForm
from posts.models import Post

# Con el decorador, se usa como middleware, de autenticacion, en caso de no estar autenticado
# redireccionara la pagina a la variable definida en settings.py LOGIN_URL



@login_required
def list_posts(request: WSGIRequest):
    # trayendo los post por orden de cracion descendente
    posts: List[Post] = Post.objects.all().order_by('-created_at')
    # Retornando la vista
    return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def create_post(request: WSGIRequest):
    """Create new post view"""
    if request.method == 'POST':
        form: PostForm = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Si esta correcto se puede guardar de una ves en la bd
            form.save()
            return redirect('feeds')
    else:
        form: PostForm = PostForm()
    return render(request, template_name='posts/new.html',
                  context={'form': form, 'user': request.user, 'profile': request.user.profile})
