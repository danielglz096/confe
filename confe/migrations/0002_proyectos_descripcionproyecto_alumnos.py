# Generated by Django 4.2.7 on 2023-11-06 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
                ('periodo', models.CharField(max_length=255)),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DescripcionProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confe.proyectos')),
            ],
        ),
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=255)),
                ('institucion', models.CharField(max_length=255)),
                ('clave', models.CharField(max_length=255)),
                ('carrera', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confe.proyectos')),
            ],
        ),
    ]