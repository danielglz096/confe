from django.db import models

class Instituciones(models.Model):
    nombre = models.CharField(max_length=100)
    acronimo = models.CharField(max_length=10)
    otra_condicion = models.CharField(max_length=100)
    arrendamiento = models.CharField(max_length=100)
    horario_trabajo = models.CharField(max_length=100)
    nomina = models.IntegerField()
    voluntarios = models.IntegerField()
    registrada = models.CharField(max_length=100)
    calle_numero = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)
    delegacion = models.CharField(max_length=100)
    cp = models.IntegerField()
    estado = models.CharField(max_length=100)
    telefono = models.IntegerField()
    facebook_twitter = models.CharField(max_length=100)
    sitioweb = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=500)
    sector_marginado = models.CharField(max_length=500)
    trayectoria = models.CharField(max_length=500)
    responsable = models.CharField(max_length=100)
    telefono_responsable = models.IntegerField()
    horario_atencion = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Proyectos(models.Model):
    año = models.IntegerField()
    periodo = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    
    def __str__(self):
        return self.clave

class DescripcionProyecto(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.proyecto.nombre

class Alumnos(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    area = models.CharField(max_length=255)
    institucion = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)
    carrera = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
