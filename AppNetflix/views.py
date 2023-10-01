from django.shortcuts import render, get_object_or_404
from .models import Pelicula, Serie


# Create your views here.
def inicio(request):
    return render(request, 'AppNetflix/inicio.html')

def peliculas(request):
    peliculas = Pelicula.objects.all()

    return render(request, 'AppNetflix/peliculas.html', {'peliculas': peliculas})

def series(request):
    series = Serie.objects.all()

    return render(request, 'AppNetflix/series.html', {'series': series})

def peliculasYSeries(request):
    peliculas = Pelicula.objects.all()
    series = Serie.objects.all()
    
    return render(request, 'AppNetflix/peliculasYSeries.html', {'peliculas': peliculas, 'series': series})

def infoPelicula(request, pelicula_id):
    # Obtén la película correspondiente según su ID
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)

    return render(request, 'AppNetflix/infoPelicula.html', {'pelicula': pelicula})

def infoSerie(request, serie_id):
    # Obtén la película correspondiente según su ID
    serie = get_object_or_404(Serie, pk=serie_id)

    return render(request, 'AppNetflix/infoserie.html', {'serie': serie})