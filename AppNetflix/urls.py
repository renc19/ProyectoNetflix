"""
URL configuration for ProyectoMama project.

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
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('peliculasYSeries/', views.peliculasYSeries, name="PeliculasYSeries"),
    path('peliculas/', views.peliculas, name="Peliculas"),
    path('series/', views.series, name="Series"),
    path('infoPelicula/<int:pelicula_id>/', views.infoPelicula, name='InfoPelicula'),
    path('infoSerie/<int:serie_id>/', views.infoSerie, name='InfoSerie'),
    path('agregar/', views.agregarPeliculaSerie, name="AgregarPeliculaSerie"),
    path('agregarPelicula/', views.agregarPelicula, name="AgregarPelicula"),
    path('agregarSerie/', views.agregarSerie, name="AgregarSerie"),
    path('registroFormulario/', views.registroFormulario, name="RegistroFormulario"),
    path('buscar/', views.buscar, name='Buscar'),
]