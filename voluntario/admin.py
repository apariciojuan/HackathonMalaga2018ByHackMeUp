from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'ciudad', 'disponibilidad')
    list_display_links = ('nombre', 'apellido')

    search_fields = (
        'nombre',
        'apellido',
        'telefono',
        'ciudad',
    )

    list_filter = (
        'disponibilidad',
        'ciudad',
        'ocupacion'
    )
