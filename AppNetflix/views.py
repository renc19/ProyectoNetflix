from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pelicula, Serie, Cuenta
from .forms import RegistroFormulario, AgregarPeliculaForm, AgregarSerieForm, BuscarForm

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

def agregarPeliculaSerie(request):
    return render(request, 'AppNetflix/agregarPeliculaSerie.html')

def agregarPelicula(request):
    if request.method == 'POST':
        form = AgregarPeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            nuevaPelicula = Pelicula(
                nombre=form.cleaned_data['nombre'],
                genero=form.cleaned_data['genero'],
                duracion=form.cleaned_data['duracion'],
                descripcion=form.cleaned_data['descripcion'],
                imagen=form.cleaned_data['imagen'],
                portada=form.cleaned_data['portada']
            )
            nuevaPelicula.save()
            messages.success(request, '¡Película agregada correctamente!')
            return redirect('Peliculas')
    else:
        form = AgregarPeliculaForm()

    return render(request, 'AppNetflix/agregarPelicula.html', {'form': form})

def agregarSerie(request):
    if request.method == 'POST':
        form = AgregarSerieForm(request.POST, request.FILES)
        if form.is_valid():
            nuevaSerie = Serie(
                nombre=form.cleaned_data['nombre'],
                genero=form.cleaned_data['genero'],
                temporadas=form.cleaned_data['temporadas'],
                descripcion=form.cleaned_data['descripcion'],
                imagen=form.cleaned_data['imagen'],
                portada=form.cleaned_data['portada']
            )
            nuevaSerie.save()
            messages.success(request, '¡Serie agregada correctamente!')
            return redirect('Series')
    else:
        form = AgregarSerieForm()

    return render(request, 'AppNetflix/agregarSerie.html', {'form': form})

def buscar(request):
    terminoBusqueda = request.GET.get('terminoBusqueda', '')

    resultadosPeliculas = Pelicula.objects.filter(nombre__icontains=terminoBusqueda)
    resultadosSeries = Serie.objects.filter(nombre__icontains=terminoBusqueda)

    form = BuscarForm(initial={'terminoBusqueda': terminoBusqueda})

    return render(request, 'AppNetflix/buscar.html', {
        'form': form,
        'resultadosPeliculas': resultadosPeliculas,
        'resultadosSeries': resultadosSeries,
    })

def registroFormulario(request):                       
    if request.method == 'POST':                       # De esta manera podremos guardar los datos utilizando formularios de DJANGO.
        
        miFormulario = RegistroFormulario(request.POST)    #aqui me llega toda la informacion del html
        
        print(miFormulario)

        if miFormulario.is_valid():   # Si pasa la validacion de DJANGO
            informacion = miFormulario.cleaned_data

            cuenta = Cuenta(
                usuario=informacion['usuario'], 
                contraseña=informacion['contraseña'],
                nombre=informacion['nombre'],  
                apellido=informacion['apellido']
                )    
            
            cuenta.save()

            messages.success(request, '¡Registro exitoso!')

            return render(request, "AppNetflix/inicio.html")  # Vuelve a donde se le diga.
    
    else:
        miFormulario = RegistroFormulario()    # Formulario vacio para construir el html

    return render(request, "AppNetflix/registroFormulario.html", {"miFormulario":miFormulario})
