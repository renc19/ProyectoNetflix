from django.db import models
from django.contrib.auth.hashers import make_password

class Cuenta(models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=128, default='')  # Aumentamos la longitud para contraseñas seguras
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        # Si la contraseña no está establecida o es una contraseña en texto plano,
        # aplicamos make_password para almacenarla de forma segura.
        if not self.contraseña.startswith(('pbkdf2_sha256$', 'bcrypt', 'argon2')):
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.usuario
    
class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    duracion = models.CharField(max_length=8)   # HH:MM:SS
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='AppNetflix/assets/img/peliculas/', default='default.jpg')
    # La imagen debe ser de 450x300
    # el nombre debe ser "Nombredepelicula.jpg" sin espacios
    # el archivo .jpg debe encontrarse en AppNetflix/assets/img/peliculas/
    portada = models.ImageField(upload_to='AppNetflix/assets/img/portadas/', default='default.jpg')
    # Portadas preferiblemente 1000x1500

class Serie(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    temporadas = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='AppNetflix/assets/img/series/', default='default.jpg')     
    # La imagen debe ser de 450x300
    # el nombre debe ser "Nombredeserie.jpg" sin espacios
    # el archivo .jpg debe encontrarse en AppNetflix/assets/img/series/
    portada = models.ImageField(upload_to='AppNetflix/assets/img/portadas/', default='default.jpg')
    # Portadas preferiblemente 1000x1500