"""
GusInstragram URLs module.
"""

from django.contrib import admin
from django.urls import path
from instagus import views
from django.conf import settings
from django.conf.urls.static import static

from posts import views as post_views
from users import views as users_views

# Configuracion para que en el admin dashboard se puedan ver las imagenes de contenido estatico
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
                  path('admin/', admin.site.urls),  # urls de admin
                  path('hello-world', views.hello_world, name='hello_world_name'),
                  path('params-query', views.params_query, name='params_query'),  # /params-query?name=gus&age=25&years=2020,2021
                  path('params-url/<str:name>/<int:age>', views.params_url),  # /params-url/gus/25

                  path('', post_views.list_posts, name='feeds'),
                  path('posts/new/', post_views.create_post, name='create_post'),

                  path('users/login/', users_views.login_view, name='login'),
                  path('users/logout/', users_views.logout_view, name='logout'),
                  path('users/signup/', users_views.signup, name='signup'),
                  path('users/me/profile', users_views.update_profile, name='update_profile')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
