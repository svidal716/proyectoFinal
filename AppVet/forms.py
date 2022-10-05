from distutils.command.install_egg_info import to_filename
from email.policy import default
from msilib.schema import Control
from sys import maxsize
from tkinter import Widget
from tkinter.tix import Tree
from django import forms
from django.conf import settings
from AppVet.choices import *
from django.forms.widgets import NumberInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppVet.models import *


especieMascota = ["Perro", "Gato", "Otra"]
sexoMascota = ["Macho", "Hembra"]
vacunaMascota = ["Primovacunación", "Polivalente", "Ref Polivalente", "Rabia"]

####################################################################################################################################################
# -------------  FORMULARIO VETERINARIO ------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el formulario para los veterinarios:


class VeterinarioForm(forms.Form):

    # creamos los campos del formulario:

    nombreVetForm = forms.CharField(max_length=40, label="Nombre Veterinario")
    apellidoVetForm = forms.CharField(
        max_length=40, label="Apellido Veterinario")

    matriculaVetForm = forms.IntegerField(label="Matricula Veterinario")

    fechaNacimientoVetForm = forms.DateField(
        widget=NumberInput(attrs={'type': 'date'}), label="Fecha Nacimiento Veterinario")

    emailVetForm = forms.EmailField(label="E-Mail Veterinario")
    telefonoVetForm = forms.IntegerField(label="Telefono Veterinario")


####################################################################################################################################################
# -------------  FORMULARIO PROPIETARIO ------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el formulario para los Propietarios:
class PropietarioForm(forms.Form):

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


####################################################################################################################################################
# -------------  FORMULARIO MASCOTA-----------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el formulario para las Mascotas:
class MascotaForm(forms.Form):

    nombreMascotaForm = forms.CharField(max_length=40, label="Nombre Mascota")
    razaMascotaForm = forms.CharField(max_length=40, label="Raza Mascota")

    especieMascotaForm = forms.ChoiceField(
        choices=especie_choice, label="Especie Macota", initial='Especie Macota', widget=forms.Select(), required=True)

    fechaNacimientoMascotaForm = forms.DateField(
        widget=NumberInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")

    apellidoPropietarioMascotaForm = forms.ModelChoiceField(label="Dueño de Mascota",
                                                            queryset=DatosPropietario.objects.all())

    imagenMascotaForm = forms.ImageField(label="Imagen Mascota")


####################################################################################################################################################
# -------------  FORMULARIO Historia Clinica  ------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el formulario para los Propietarios:


class HistoriaClinicaForm(forms.Form):

    fechaConsultaForm = forms.DateField(
        widget=NumberInput(attrs={'type': 'date'}), label="Fecha de Consulta")
    nombreMascotaForm = forms.ModelChoiceField(label="Nombre de Mascota",
                                               queryset=DatosMascota.objects.all())
    sexoMascotaForm = forms.ChoiceField(label="Sexo Macota", widget=forms.Select(
        choices=sexo_choice), required=True)

    pesoMascotaForm = forms.FloatField(label="Peso Mascota (kg)")

    enfermedadPreviaMascotaForm = forms.CharField(
        max_length=100, label="Enfermedades Previas")

    vacunasMascotasForm = forms.ChoiceField(label="Vacunas Macota", widget=forms.Select(
        choices=vacunas_choice), required=True)

    comidaMascotaForm = forms.CharField(
        max_length=40, label="Alimento Mascota")
    temperaturaMascotaForm = forms.FloatField(label="Temperatura Mascota")
    motivoConsultaForm = forms.CharField(
        max_length=250, label="Motivo Consulta")
    diagnosticoMascotaForm = forms.CharField(
        max_length=350, label="Diagnostico Consulta")
    veterinarioMascotaForm = forms.ModelChoiceField(label="Veterinario",
                                                    queryset=DatosVeterinarios.objects.all())


####################################################################################################################################################
# -------------  FORMULARIO USUARIOS ---------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el formulario para los Usuarios:
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label='Modificar Nombre')
    last_name = forms.CharField(label='Modificar Apellido')
    avatar = forms.ImageField(label="Imagen")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2',
                  'first_name', 'last_name', 'avatar']
        help_texts = {k: "" for k in fields}


####################################################################################################################################################
# -------------  FORMULARIO AVATAR ------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el formulario para los Avatares:
class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")
