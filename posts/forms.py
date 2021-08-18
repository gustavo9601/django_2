from django import forms

from posts.models import Post


# Clase que herada de model form, para hacer mas eficiente todas las validaciones
# las tomara en la definicion del modelo asignao en model
class PostForm(forms.ModelForm):
    class Meta:
        # Especifica a que modelo hace referencia
        model = Post
        # Especifica los campos a mostrar
        fields = ('user', 'profile', 'title', 'photo')
