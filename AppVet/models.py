from django.db import models

# Create your models here.

# Definimos el Model Veterinarios donde se agregaran los veterinarios que trabajan.


class datosVeterinarios(models.Model):

    nombreVet = models.CharField(max_length=30)
    apellidoVet = models.CharField(max_length=30)
    fechaNacimientoVet = models.DateField()
    matriculaVet = models.IntegerField(max_length=10)
    emailVet = models.EmailField(max_length=254)
    telefonoVet = models.PhoneNumberField()


# Definimos el Model Datos Dueño de la Mascota:

class datosPropietario(models.Model):

    nombrePropietario = models.CharField(max_length=30)
    apellidoPropietario = models.CharField(max_length=30)
    fechaNacimientoPropietario = models.DateField()
    dniPropietario = models.IntegerField(max_length=10)
    emailPropietario = models.EmailField(max_length=254)
    direccionPropietario = models.CharField(max_length=200)
    barrioPropietario = models.CharField(max_length=30)
    ciudadPropietario = models.CharField(max_length=50)
    telefonoPropietario = models.PhoneNumberField()


# Definimos el Model Datos principales de la Mascota:

class datosMascota(models.Model):

    nombreMascota = models.CharField(max_length=30)
    razaMascota = models.CharField(max_length=50)
    # ----------------------------modificar lista
    especieMascota = models.CharField()
    fechaNacimientoMascota = models.DateField()

# Definimos el Model historia Clinica de la Mascota.


class historiaClinica(models.Model):

    fechaConsulta = models.DateTimeField()
    # -------- Lista con Macho / Hembra
    sexoMascota = models.CharField(max_length=30)
    pesoMascota = models.FloatField(max_length=5)
    colorMascota = models.CharField(max_length=30)
    enfermedadPreviaMascota = models.CharField(max_length=250)
    # -------- Checkbox con las vacunas.
    vacunasMascotas = models.CharField(max_length=100)
    # -------- Lista (Balanceado / Varios )
    comidaMascota = models.CharField(max_length=100)
    temperaturaMascota = models.FloatField(max_length=5)
    motivoConsulta = models.CharField(max_length=250)
    diagnosticoMascota = models.CharField(max_length=350)
    # -----> Seleccionar de la lista de Veterinarios Agregados.
    veterinarioMascota = models.CharField(max_length=50)
