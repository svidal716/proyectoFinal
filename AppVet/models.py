from tkinter import CASCADE
from django.db import models
from AppVet.choices import *
from django.contrib.auth.models import User

# Create your models here.

# Definimos el Model Veterinarios donde se agregaran los veterinarios que trabajan.


####################################################################################################################################################
# -------------  MODEL VETERINARIO -----------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el Model para los Veterinarios:
class DatosVeterinarios(models.Model):

    nombreVet = models.CharField(max_length=30)
    apellidoVet = models.CharField(max_length=30)
    fechaNacimientoVet = models.DateField()
    matriculaVet = models.IntegerField()
    emailVet = models.EmailField(max_length=254)
    telefonoVet = models.IntegerField()

    def __str__(self):
        return self.apellidoVet


####################################################################################################################################################
# -------------  MODEL PROPIETARIOS ----------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el Model para los Propietarios:

class DatosPropietario(models.Model):

    nombrePropietario = models.CharField(max_length=30)
    apellidoPropietario = models.CharField(max_length=30)
    fechaNacimientoPropietario = models.DateField()
    dniPropietario = models.IntegerField()
    emailPropietario = models.EmailField(max_length=254)
    direccionPropietario = models.CharField(max_length=200)
    barrioPropietario = models.CharField(max_length=30)
    ciudadPropietario = models.CharField(max_length=50)
    telefonoPropietario = models.IntegerField()

    def __str__(self):
        return self.apellidoPropietario


####################################################################################################################################################
# -------------  MODEL MASCOTA ---------------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el Model para las Mascotas
class DatosMascota(models.Model):

    nombreMascota = models.CharField(max_length=30)
    razaMascota = models.CharField(max_length=50)
    # ----------------------------modificar lista
    especieMascota = models.CharField(max_length=30)
    fechaNacimientoMascota = models.DateField()
    apellidoPropietarioMascota = models.ForeignKey(
        DatosPropietario, on_delete=models.CASCADE, null=True)
    imagenMascota = models.ImageField(
        upload_to='mascotas', null=True, blank=True)

    def __str__(self):
        return self.nombreMascota


####################################################################################################################################################
# -------------  MODEL HISTORIA CLINICA  -----------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el Model para las historias clinicas:


class HistoriaClinica(models.Model):

    fechaConsulta = models.DateField()
    nombreMascota = models.ForeignKey(
        DatosMascota, on_delete=models.CASCADE, null=True)
    sexoMascota = models.CharField(max_length=30)
    pesoMascota = models.FloatField()
    enfermedadPreviaMascota = models.CharField(max_length=250)
    vacunasMascotas = models.CharField(max_length=100)
    comidaMascota = models.CharField(max_length=100)
    temperaturaMascota = models.FloatField()
    motivoConsulta = models.CharField(max_length=250)
    diagnosticoMascota = models.CharField(max_length=350)
    veterinarioMascota = models.ForeignKey(
        DatosVeterinarios, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombreMascota

####################################################################################################################################################
# -------------  MODEL AVATAR ----------------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el Model para los  Avatares:


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return self.user.username


# class ImagenMascota(models.Model):
#     mascota = models.OneToOneField(DatosMascota, on_delete=models.CASCADE)
#     imagen = models.ImageField(upload_to='mascotas', null=True, blank=True)

#     def __str__(self):
#         return self.mascota.nombreMascota
