from django.contrib import admin
from users.models import Profile


# Se registran los modelos a visualizar desde el administrador
# admin.site.register(Profile)

# registrando el modelo orientado a clases
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    # model__atribute  // accede a la relacion definida en el modelo

    # indicando cual es el orden de los campos a mostrar en el admin dashboard
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # indicando a los links de relaciones del modelo el orden dy campos a mostrar
    list_display_links = ('pk', 'user')
    # permite idnciar en el dashboard que los campos e podran editar en la tabla sin entrar al detalle
    list_editable = ('phone_number', 'website', 'picture')
    # permite indicar el filter sobre que campos se aplicara en el form de las tablas
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    # permite indicar que campos se comportan como botones de filtro
    list_filter = ('created_at', 'updated_at', 'user__is_active')
    # permite indicar la organizacion de los campos de edicion para el modelo
    # ('Titulo': {campos y organizacion a mostrar})
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),)
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created_at', 'updated_at',))
        })
    )
    # especificando que campos aunque sean visibles en el dashboard sean solo de lectura
    readonly_fields = ('created_at', 'updated_at')
