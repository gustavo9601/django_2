from django.db import models
from django.contrib.auth.models import User

from users.models import Profile


class UserManual(models.Model):
    """User Model"""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True)
    birthdate = models.DateField(blank=True, null=True)  # blank = null
    is_admin = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)  # Fecha automatica
    modified = models.DateTimeField(auto_now=True)  # Fecha cada ves que se actualice

    def __str__(self):
        """Return info user"""
        return f"""
        email: {self.email}
        password: {self.password}
        first_name: {self.first_name}
        last_name: {self.last_name}
        bio: {self.bio}
        birthdate: {self.birthdate}
        is_admin: {self.is_admin}
        created: {self.created}
        modified: {self.modified}
        """


"""
Post Model
"""


class Post(models.Model):
    """Post model"""

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Llave foranea
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by @{self.user.username}"
