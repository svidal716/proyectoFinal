from email.policy import default
from sys import maxsize
from tkinter import Widget
from django import forms
from django.conf import settings
from AppVet.choice import *
from django.forms.widgets import NumberInput


# Creamos el Formulario general para la primera entrega.

especieMascota = ["Perro", "Gato", "Otra"]
sexoMascota = ["Macho", "Hembra"]
vacunaMascota = ["Primovacunación", "Polivalente", "Ref Polivalente", "Rabia"]


class veterinarioForm(forms.Form):

    # creamos los campos del formulario:

    nombreVetForm = forms.CharField(max_length=40, label="Nombre Veterinario")
    apellidoVetForm = forms.CharField(
        max_length=40, label="Apellido Veterinario")

    matriculaVetForm = forms.IntegerField(label="Matricula Veterinario")

    fechaNacimientoVetForm = forms.DateField(
        widget=NumberInput(attrs={'type': 'date'}), label="Fecha Nacimiento Veterinario")

    emailVetForm = forms.EmailField(label="E-Mail Veterinario")
    telefonoVetForm = forms.IntegerField(label="Telefono Veterinario")


class propietarioForm(forms.Form):

    nombrePropietarioForm = forms.CharField(
        max_length=40, label="Nombre Dueño")

    apellidoPropietarioForm = forms.CharField(
        max_length=40, label="Apellido Dueño")

    fechaNacimientoPropietarioForm = forms.DateField(
        widget=NumberInput(attrs={'type': 'date'}), label="Fecha de Nacimiento Propietario")

    dniPropietarioForm = forms.IntegerField(label="DNI Dueño")

    emailPropietarioForm = forms.EmailField(label="E-Mail Veterinario")

    direccionPropietarioForm = forms.CharField(
        max_length=100, label="Domicilio Dueño")

    barrioPropietarioForm = forms.CharField(
        max_length=40, label="Barrio Dueño")

    ciudadPropietarioForm = forms.CharField(
        max_length=40, label="Ciudad Dueño")

    telefonoPropietarioForm = forms.IntegerField(label="Telefono Dueño")


class mascotaForm(forms.Form):

    nombreMascotaForm = forms.CharField(max_length=40, label="Nombre Mascota")
    razaMascotaForm = forms.CharField(max_length=40, label="Raza Mascota")

    especieMascotaForm = forms.ChoiceField(
        choices=especie_choice, label="Especie Macota", initial='Especie Macota', widget=forms.Select(), required=True)

    fechaNacimientoMascotaForm = forms.DateField(
        widget=NumberInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")


class historiaForm(forms.Form):

    fechaConsultaForm = forms.DateField()

    # -------- Lista con Macho / Hembra
    sexoMascotaForm = forms.ChoiceField(
        choices=sexo_choice, label="Sexo Macota", initial='Sexo Macota', widget=forms.Select(), required=True)

    pesoMascotaForm = forms.FloatField(label="Peso Mascota (kg)")
    colorMascotaForm = forms.CharField(
        max_length=20, label="Color de la Mascota")

    enfermedadPreviaMascotaForm = forms.CharField(
        max_length=100, label="Enfermedades Previas")

    vacunasMascotasForm = forms.ChoiceField(
        choices=vacunas_choice, label="Vacuna Macota", initial='Vacunas Macota', widget=forms.Select(), required=True)

    comidaMascotaForm = forms.CharField(
        max_length=40, label="Alimento Mascota")
    temperaturaMascotaForm = forms.FloatField(label="Temperatura Mascota")
    motivoConsultaForm = forms.CharField(
        max_length=400, label="Motivo Consulta")
    diagnosticoMascotaForm = forms.CharField(
        max_length=400, label="Diagnostico")

    # -----> Seleccionar de la lista de Veterinarios Agregados.
    veterinarioMascotaForm = forms.CharField(
        max_length=80, label="Veterinario ")
