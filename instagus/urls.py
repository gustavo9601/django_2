"""
GusInstragram URLs module.
"""

from django.contrib import admin
from django.urls import path
from instagus import views

from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls), # urls de admin
    path('hello-world', views.hello_world),
    path('params-query', views.params_query), # /params-query?name=gus&age=25&years=2020,2021
    path('params-url/<str:name>/<int:age>', views.params_url), # /params-url/gus/25

    path('posts/', post_views.list_posts)
]
