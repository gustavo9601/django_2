# Django
from sqlite3 import IntegrityError

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/posts/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Usando la autenticacion por default de dejango
        user = authenticate(request, username=username, password=password)

        if user:
            # Inicializa las sesiones por default
            login(request, user)
            # Redirecciona pasando por parametro el nombre de la url, o el propio path
            return redirect('feeds')
        else:
            return render(request, 'users/login.html', {'error': 'Invalidate username or password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            # Creando el usuario
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        # Completando los siguientes cambios
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def update_profile(request):

    profile = request.user.profile
    user = request.user
    if request.method == 'POST':
        # Usando una clase de form request, se le pasa la info por post, y si se envian archivos FILES
        form: ProfileForm = ProfileForm(request.POST, request.FILES)
        # Si todas las validaciones pasaron
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(request, 'users/update_profile.html',
                  context={
                      'profile': profile,
                      'user': user,
                      'form': form
                  })
