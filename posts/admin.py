from django.contrib import admin

from posts.models import Post


# Register your models here.

# registrando el modelo orientado a clases
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""