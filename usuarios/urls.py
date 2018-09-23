from django.urls import path, include
from .views import RegistroUsuario

#me trae las url de accounts sin necesitas usar accounts en la url
app_name = "accounts"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registrar/', RegistroUsuario.as_view(), name='registrar'),
]
