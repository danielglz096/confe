from rest_framework import serializers
from .models import Instituciones, Proyectos, DescripcionProyecto, Alumnos

class InstitucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituciones
        fields = ['id', 'nombre', 'acronimo', 'otra_condicion', 'arrendamiento', 'horario_trabajo', 'nomina', 'voluntarios', 'registrada', 'calle_numero', 'colonia', 'delegacion', 'cp', 'estado', 'telefono', 'facebook_twitter', 'sitioweb', 'objetivo', 'sector_marginado', 'trayectoria', 'responsable', 'telefono_responsable', 'horario_atencion', 'correo']

class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = ['id', 'año', 'periodo', 'clave', 'nombre', 'estado']

class DescripcionProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescripcionProyecto
        fields = ['id', 'proyecto', 'descripcion']

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ['id_estudiante', 'area', 'institucion', 'clave', 'carrera', 'nombre', 'proyecto']