# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ficha(models.Model):
    itb = models.FloatField(blank=True, null=True)
    tempamb = models.FloatField(blank=True, null=True)
    tiempodm = models.IntegerField(blank=True, null=True)
    dfc = models.BooleanField(blank=True, null=True)
    tiempodfc = models.IntegerField(blank=True, null=True)
    rut = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='rut', blank=True, null=True)
    imagenes = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha'


class Paciente(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    primer_nombre = models.CharField(max_length=255, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=255, blank=True, null=True)
    primer_apellido = models.CharField(max_length=255, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'
