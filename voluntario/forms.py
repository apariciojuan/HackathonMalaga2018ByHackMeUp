from .models import Person, dias, ciudades, ocupaciones, rangoHorario
from django import forms



class SearchForm(forms.Form):
    Disponibilidad = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=dias, required=False)
    Ciudades = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            choices=ciudades, required=False)
    Ocupacion = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            choices=ocupaciones, required=False)
    FranjaHorario = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            choices=rangoHorario, required=False)


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
            'franjaHoraria',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'ocupacion': 'Ocupacion',
            'ciudad': 'Ciudad',
            'disponibilidad': 'Disponibilidad',
            'franjaHoraria': 'Franja Horaria',
        }
        widgets = {

            # 'ciudad': forms.CheckboxSelectMultiple(),
            # 'ocupacion': forms.CheckboxSelectMultiple(),
            # 'disponibilidad': forms.CheckboxSelectMultiple(),
}
