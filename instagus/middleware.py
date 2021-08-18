from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Profile completion middleware
        Ensure every user that is interacting with the platform
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """code to be extecuted for each request before the view is called."""
        # is_anonymous // valor que retorna gracias a la autenticacion propia de django
        if not request.user.is_anonymous:
            # Verifica que no sea usuario admin del staff para que no aplique el middleware
            if not request.user.is_staff:
                # Accede a la relacion uno a uno de usario a profile
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    # reverse // a partir del parametro nombre del path devuelve la ruta
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')
        # Si ya tiene los datos en el perfil, se deja pasar el middleware
        return self.get_response(request)