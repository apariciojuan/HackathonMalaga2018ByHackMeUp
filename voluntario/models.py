from django.db import models

ciudades = (
    ('Malaga', 'Malaga'),
    ('Sevilla', 'Sevilla'),
    ('Madrid', 'Madrid'),
    ('Barcelona', 'Barcelona'),
)

horas = (
    ('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'),
    ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'),
    ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'),
    ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'),
    ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'),
    ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'),
    ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'),
    ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00'),
    ('--', '--'),
)


class horario(models.Model):
    fromto = models.CharField(choices=horas, default='--', verbose_name="From:", max_length=8)
    to = models.CharField(choices=horas, default='--', verbose_name="To:", max_length=8)

    def __str__(self):
        return "{} {}".format(self.fromto, self.to)


class DiasDisponibles(models.Model):
    Lunes = models.ManyToManyField(horario, related_name='lunes_set', blank=True)
    Martes = models.ManyToManyField(horario, related_name='martes_set', blank=True)
    Miercoles = models.ManyToManyField(horario, related_name='miercoles_set', blank=True)
    Jueves = models.ManyToManyField(horario, related_name='jueves_set', blank=True)
    Viernes = models.ManyToManyField(horario, related_name='viernes_set', blank=True)
    Sabado = models.ManyToManyField(horario, related_name='sabado_set', blank=True)
    Domingo = models.ManyToManyField(horario, related_name='domingo_set', blank=True)


class Person(models.Model):
    nombre= models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=100, choices=ciudades)
    disponibilidad = models.ForeignKey(DiasDisponibles, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

    class Meta:
        ordering = ['-id']
