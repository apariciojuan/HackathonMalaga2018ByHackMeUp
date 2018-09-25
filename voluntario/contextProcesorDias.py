def context_data(request):

    dias = [ 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes',
             'Sabado', 'Domingo' ]

    return {'dias': dias }
