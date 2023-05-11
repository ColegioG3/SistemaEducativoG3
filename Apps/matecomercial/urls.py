"""
URL configuration for ColegioG3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Apps.matecomercial import views
from .views import PrimeraUnidadView, PUFraccionesView, OpeFraccionesView, ProporcionalidadView, SociedadesView, AligacionesView, AleacionesView, TantoporCientoView, PrimeraUnidadEjView, OpeFraccionesEjView

app_name = 'matecomercial'

urlpatterns = [
    path('MateComercial', PrimeraUnidadView.as_view(), name='macomercialapp'),
    path('fracciones/', PUFraccionesView.as_view(), name='fraccionesapp'),
    path('OperacionesConFracciones/', OpeFraccionesView.as_view(), name='operacioesfraccionesapp'),
    path('Proporcionalidad/', ProporcionalidadView.as_view(), name='proporcionalidadapp'),
    path('Sociedades/', SociedadesView.as_view(), name='sociedadesapp'),
    path('Aligaciones/',AligacionesView.as_view(), name='aligacionesapp'),
    path('Aleaciones/',AleacionesView.as_view(), name='aleacionesapp'),
    path('TantoPorCiento/',TantoporCientoView.as_view(), name='porcientoapp'),
    path('MateComercialEjercicios', PrimeraUnidadEjView.as_view(), name='macomercialEjapp'),
    path('FraccionesEjercicios/',OpeFraccionesEjView.as_view(), name='fraccionesej'),
]