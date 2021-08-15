from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model

    Proxy model that extends the base data with other information
    """
    # Creando una realacion de uno a uno
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    # De tipo imagen, almacenara la ruta, pero permitira hacer validaciones a futuro
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return Profile basic"""
        return f"""
        username: {self.user.username}
        first_name: {self.user.first_name}
        last_name: {self.user.last_name}
        """
