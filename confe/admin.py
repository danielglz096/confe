from django.contrib import admin
from .models import Instituciones, Proyectos, DescripcionProyecto, Alumnos

admin.site.register(Instituciones)
admin.site.register(Proyectos)
admin.site.register(DescripcionProyecto)
admin.site.register(Alumnos)