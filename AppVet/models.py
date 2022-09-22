from django.db import models
from AppVet.choice import *
from django.contrib.auth.models import User

# Create your models here.

# Definimos el Model Veterinarios donde se agregaran los veterinarios que trabajan.


class DatosVeterinarios(models.Model):

    nombreVet = models.CharField(max_length=30)
    apellidoVet = models.CharField(max_length=30)
    fechaNacimientoVet = models.DateField()
    matriculaVet = models.IntegerField()
    emailVet = models.EmailField(max_length=254)
    telefonoVet = models.IntegerField()

    def __str__(self):
        return self.nombreVet+" "+str(self.apellidoVet)+" "+str(self.fechaNacimientoVet)+" "+str(self.matriculaVet)+" "+str(self.emailVet)+" "+str(self.telefonoVet)


# Definimos el Model Datos Dueño de la Mascota:

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


# Definimos el Model Datos principales de la Mascota:

class DatosMascota(models.Model):

    nombreMascota = models.CharField(max_length=30)
    razaMascota = models.CharField(max_length=50)
    # ----------------------------modificar lista

    especieMascota = models.CharField(max_length=30)
    fechaNacimientoMascota = models.DateField()

# Definimos el Model historia Clinica de la Mascota.


class HistoriaClinica(models.Model):

    fechaConsulta = models.DateField()
    # -------- Lista con Macho / Hembra
    sexoMascota = models.CharField(max_length=30)
    pesoMascota = models.FloatField()
    colorMascota = models.CharField(max_length=30)
    enfermedadPreviaMascota = models.CharField(max_length=250)
    # -------- Checkbox con las vacunas.
    vacunasMascotas = models.CharField(max_length=100)
    # -------- Lista (Balanceado / Varios )
    comidaMascota = models.CharField(max_length=100)
    temperaturaMascota = models.FloatField()
    motivoConsulta = models.CharField(max_length=250)
    diagnosticoMascota = models.CharField(max_length=350)
    # -----> Seleccionar de la lista de Veterinarios Agregados.
    veterinarioMascota = models.CharField(max_length=50)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares')
