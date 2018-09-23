from django.db import models

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

ciudades = (
    ('Malaga', 'Malaga'),
    ('Sevilla', 'Sevilla'),
    ('Madrid', 'Madrid'),
    ('Barcelona', 'Barcelona'),
)

ocupaciones = (
    ('Medico', 'Medico'),
    ('Enfermero', 'Enfermero'),
    ('Abogado', 'Abogado'),
    ('Ingeniero', 'Ingeniero'),
)

rangoHorario = (
    ('Mañana', 'Mañana'),
    ('Tarde', 'Tarde'),
    ('Noche', 'Noche'),
)


class Person(models.Model):
    nombre= models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15)
    ocupacion = models.CharField(max_length=50, choices=ocupaciones)
    ciudad = models.CharField(max_length=100, choices=ciudades)
    disponibilidad = models.CharField(max_length=20, choices=dias)
    franjaHoraria = models.CharField(max_length=20, choices=rangoHorario, null=True, blank=True)


    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

    class Meta:
        ordering = ['-id']
