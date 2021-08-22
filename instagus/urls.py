"""
GusInstragram URLs module.
"""

from django.contrib import admin
from django.urls import path, include
from instagus import views
from django.conf import settings
from django.conf.urls.static import static

from posts import views as post_views
from users import views as users_views

# Configuracion para que en el admin dashboard se puedan ver las imagenes de contenido estatico
# + static(settings.        MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
                  path('admin/', admin.site.urls),  # urls de admin
                  path('hello-world', views.hello_world, name='hello_world_name'),
                  path('params-query', views.params_query, name='params_query'),
                  # /params-query?name=gus&age=25&years=2020,2021
                  path('params-url/<str:name>/<int:age>', views.params_url),  # /params-url/gus/25

                  # Separando la logica de las rutas en otro archivo
                  # incluye el archivo de rotas y define el subnombre posts.
                  path('', include(('posts.urls', 'posts'), namespace='posts')),

                  # separando la logica de usuarios
                  path('', include(('users.urls', 'users'), namespace='users'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
