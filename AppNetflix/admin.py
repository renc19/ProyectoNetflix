from django.contrib import admin
from .models import Cuenta, Pelicula, Serie

# Register your models here.
admin.site.register(Cuenta)
admin.site.register(Pelicula)
admin.site.register(Serie)