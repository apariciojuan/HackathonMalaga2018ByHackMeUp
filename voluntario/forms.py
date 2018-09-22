from .models import Person, dias, ciudades, ocupaciones
from django import forms



class SearchForm(forms.Form):
    Disponibilidad = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=dias, required=False)
    Ciudades = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            choices=ciudades, required=False)
    Ocupacion = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            choices=ocupaciones, required=False)


class PersonCreateForm(forms.ModelForm):

    class Meta():
        model = Person
        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'ocupacion',
            'ciudad',
            'disponibilidad',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'ocupacion': 'Ocupacion',
            'ciudad': 'Ciudad',
            'disponibilidad': 'Disponibilidad',
        }
        widgets = {

             'ciudad': forms.CheckboxSelectMultiple(),
             'ocupacion': forms.CheckboxSelectMultiple(),
             'disponibilidad': forms.CheckboxSelectMultiple(),
}
