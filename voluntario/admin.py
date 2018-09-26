from django.contrib import admin
from .models import Person, DiasDisponibles, horario
# Register your models here.

 #De esta forma puedo hacer que muestre el modelo comoyo quiero
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    #Muestra los campos que declaro en la lista de objetos
    list_display = ('nombre', 'apellido', 'telefono', 'ciudad')
    #hace clickeable los campos estos para ir al detalle del objeto
    list_display_links = ('nombre', 'apellido')

    #asi agrego un campò de busqueda dentro de modelo y los campos en los
    #que quiero que busque
    search_fields = (
        'nombre',
        'apellido',
        'telefono',
        'ciudad',
    )

    #Estos son los filtros que le ponemos a un costado para filtrar
    #los resultados
    list_filter = (
        'disponibilidad',
        'ciudad',
    )

admin.site.register(DiasDisponibles)
admin.site.register(horario)
