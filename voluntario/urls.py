"""hackmeup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'voluntario'

urlpatterns = [
    path('', HomeList.as_view(), name='home'),
    path('filter/', PersonListFilter, name='list_filter_person'),
    path('nuevaPersona/', PersonCreate.as_view(), name='crear_persona'),
    path('verPersona/<int:pk>/', PersonVer.as_view(), name='ver_person'),
    path('EditPerson/<int:pk>/', PersonUpdate.as_view(), name='edit_person'),
    path('borrarPerson/<int:pk>/', PersonDelete.as_view(), name='borrar_person'),
]
