from .models import Person, ciudades, DiasDisponibles
from django import forms

dias = (
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miercoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sabado', 'Sabado'),
    ('Domingo', 'Domingo'),
    ('All', 'All'),
)


class SearchForm(forms.Form):
    Disponibilidad = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=dias, required=False)
    Ciudades = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            choices=ciudades, required=False)


class PersonCreateForm(forms.ModelForm):

    class Meta():
        model = Person
        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'ocupacion',
            'ciudad',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'ocupacion': 'Ocupacion',
            'ciudad': 'Ciudad',
        }
        widgets = {
            #'date': forms.TextInput(attrs={'class':'datepicker'}),
            # 'ciudad': forms.CheckboxSelectMultiple(),
            # 'ocupacion': forms.CheckboxSelectMultiple(),
            # 'disponibilidad': forms.CheckboxSelectMultiple(),
}


class DiasDisponiblesCreateForm(forms.ModelForm):

    class Meta():
        model = DiasDisponibles
        fields = '__all__'
