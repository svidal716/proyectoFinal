from distutils.command.install_egg_info import to_filename
from email.policy import default
from msilib.schema import Control
from sys import maxsize
from tkinter import Widget
from tkinter.tix import Tree
from attr import attr
from django import forms
from django.conf import settings
from AppVet.choices import *
from django.forms.widgets import NumberInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppVet.models import *
from AppVet.choices import *
from ckeditor.widgets import CKEditorWidget

especieMascota = ["Perro", "Gato", "Otra"]
sexoChoice = [("Macho", "Macho"), "Hembra", "Hembra"]
vacunaMascota = ["Primovacunación", "Polivalente", "Ref Polivalente", "Rabia"]

####################################################################################################################################################
# -------------  FORMULARIO VETERINARIO ------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
#
#
'''
-   Definimos las campos para agregar Veterinarios.
-   Con widget le damos formato a los campos del formulario.
'''


class VeterinarioForm(forms.Form):

    nombreVetForm = forms.CharField(max_length=40, label="Nombre Veterinario", widget=forms.TextInput(
        attrs={'placeholder': 'Nombre', 'style': 'width: 300px;', 'class': 'form-control'}))
    apellidoVetForm = forms.CharField(
        max_length=40, label="Apellido Veterinario", widget=forms.TextInput(
            attrs={'placeholder': 'Apellido', 'style': 'width: 300px;', 'class': 'form-control'}))

    matriculaVetForm = forms.IntegerField(label="Matricula Veterinario", widget=forms.TextInput(
        attrs={'placeholder': 'Matricula', 'style': 'width: 150px;', 'class': 'form-control'}))

    fechaNacimientoVetForm = forms.DateField(
        widget=NumberInput(attrs={'type': 'date', 'class': 'form-control'}), label="Fecha Nacimiento Veterinario")

    emailVetForm = forms.EmailField(label="E-Mail Veterinario", widget=forms.TextInput(
        attrs={'placeholder': 'E-Mail', 'style': 'width: 300px;', 'class': 'form-control'}))
    telefonoVetForm = forms.IntegerField(label="Telefono Veterinario", widget=forms.TextInput(
        attrs={'placeholder': 'Telefono', 'style': 'width: 150px;', 'class': 'form-control'}))


####################################################################################################################################################
# -------------  FORMULARIO PROPIETARIO ------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
#
#
'''
-   Definimos las campos para agregar Propietarios / Clientes.
-   Con widget le damos formato a los campos del formulario.
'''


class PropietarioForm(forms.Form):

    nombrePropietarioForm = forms.CharField(
        max_length=40, label="Nombre Dueño", widget=forms.TextInput(
            attrs={'placeholder': 'Nombre', 'style': 'width: 300px;', 'class': 'form-control'}))

    apellidoPropietarioForm = forms.CharField(
        max_length=40, label="Apellido Dueño", widget=forms.TextInput(
            attrs={'placeholder': 'Apellido', 'style': 'width: 300px;', 'class': 'form-control'}))

    fechaNacimientoPropietarioForm = forms.DateField(
        widget=NumberInput(attrs={'type': 'date', 'class': 'form-control'}), label="Fecha de Nacimiento Propietario")

    dniPropietarioForm = forms.IntegerField(label="DNI Dueño", widget=forms.TextInput(
        attrs={'placeholder': 'DNI', 'style': 'width: 150px;', 'class': 'form-control'}))

    emailPropietarioForm = forms.EmailField(label="E-Mail Veterinario", widget=forms.TextInput(
        attrs={'placeholder': 'E-Mail', 'style': 'width: 300px;', 'class': 'form-control'}))

    direccionPropietarioForm = forms.CharField(
        max_length=100, label="Domicilio Dueño", widget=forms.TextInput(
            attrs={'placeholder': 'Domicilio', 'style': 'width: 300px;', 'class': 'form-control'}))

    barrioPropietarioForm = forms.CharField(
        max_length=40, label="Barrio Dueño", widget=forms.TextInput(
            attrs={'placeholder': 'Barrio', 'style': 'width: 200px;', 'class': 'form-control'}))

    ciudadPropietarioForm = forms.CharField(
        max_length=40, label="Ciudad Dueño", widget=forms.TextInput(
            attrs={'placeholder': 'Ciudad', 'style': 'width: 200px;', 'class': 'form-control'}))

    telefonoPropietarioForm = forms.IntegerField(label="Telefono Dueño", widget=forms.TextInput(
        attrs={'placeholder': 'Telefono', 'style': 'width: 150px;', 'class': 'form-control'}))


####################################################################################################################################################
# -------------  FORMULARIO MASCOTA-----------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
#
#
'''
-   Definimos las campos para agregar Mascotas.
-   Con widget le damos formato a los campos del formulario.
-   Relacionamos el campo apellidoPropietarioMascotaForm con el Models de Propietarios para asi  saber quien es el dueño
de la mascota.
'''


class MascotaForm(forms.Form):

    nombreMascotaForm = forms.CharField(max_length=40, label="Nombre Mascota", widget=forms.TextInput(
        attrs={'placeholder': 'Nombre', 'style': 'width: 150px;', 'class': 'form-control'}))
    razaMascotaForm = forms.CharField(max_length=40, label="Raza Mascota", widget=forms.TextInput(
        attrs={'placeholder': 'Raza', 'style': 'width: 150px;', 'class': 'form-control'}))

    especieMascotaForm = forms.ChoiceField(
        choices=especie_choice, label="Especie Macota", initial='Especie Macota', widget=forms.Select(attrs={'placeholder': 'Especie', 'style': 'width: 150px;', 'class': 'form-control'}), required=True, )

    fechaNacimientoMascotaForm = forms.DateField(
        widget=NumberInput(attrs={'type': 'date', 'class': 'form-control'}), label="Fecha de Nacimiento")

    apellidoPropietarioMascotaForm = forms.ModelChoiceField(
        label="Dueño de Mascota", queryset=DatosPropietario.objects.all())


####################################################################################################################################################
# -------------  FORMULARIO Historia Clinica  ------------------------------------------------------------------------------------------------------
####################################################################################################################################################
#
#
'''
-   Definimos las campos para agregar historias clinicas.
-   Con widget le damos formato a los campos del formulario.
-   Relacionamos campo nombreMascotaForm con el models de Mascotas para seleccionar una mascota existente. 
-   Relacionamos campo veterinarioMascotaForm con el models Veterinarios, para que cada masctoa tenga un veterinario existente.
'''


class HistoriaClinicaForm(forms.Form):

    fechaConsultaForm = forms.DateField(
        widget=NumberInput(attrs={'type': 'date', 'style': 'width: 150px;', 'class': 'form-control'}), label="Fecha de Consulta")
    nombreMascotaForm = forms.ModelChoiceField(label="Nombre de Mascota",
                                               queryset=DatosMascota.objects.all(), widget=forms.Select(attrs={'placeholder': 'Sexo', 'style': 'width: 150px;', 'class': 'form-control'}))
    sexoMascotaForm = forms.ChoiceField(label="Sexo Macota", choices=sexo_choice, widget=forms.Select(
        attrs={'placeholder': 'Sexo', 'style': 'width: 150px;', 'class': 'form-control'}), required=True)

    pesoMascotaForm = forms.FloatField(label="Peso Mascota (kg)", widget=forms.TextInput(
        attrs={'placeholder': 'Peso', 'style': 'width: 150px;', 'class': 'form-control'}))

    enfermedadPreviaMascotaForm = forms.CharField(
        max_length=100, label="Enfermedades Previas", widget=forms.TextInput(
            attrs={'placeholder': 'Enfermedades', 'style': 'width: 250px;', 'class': 'form-control'}))

    vacunasMascotasForm = forms.ChoiceField(label="Vacunas Macota", choices=vacunas_choice, widget=forms.Select(
        attrs={'placeholder': 'Vacunas', 'style': 'width: 250px;', 'class': 'form-control'}), required=True)

    comidaMascotaForm = forms.CharField(
        max_length=40, label="Alimento Mascota", widget=forms.TextInput(
            attrs={'placeholder': 'Alimento', 'style': 'width: 250px;', 'class': 'form-control'}))
    temperaturaMascotaForm = forms.FloatField(label="Temperatura Mascota", widget=forms.TextInput(
        attrs={'placeholder': 'Temperatura', 'style': 'width: 150px;', 'class': 'form-control'}))
    motivoConsultaForm = forms.CharField(
        max_length=250, label="Motivo Consulta", widget=CKEditorWidget())
    diagnosticoMascotaForm = forms.CharField(
        max_length=350, label="Diagnostico Consulta", widget=CKEditorWidget())
    veterinarioMascotaForm = forms.ModelChoiceField(label="Veterinario",
                                                    queryset=DatosVeterinarios.objects.all(), widget=forms.Select(attrs={'style': 'width: 150px;', 'class': 'form-control'}))


####################################################################################################################################################
# -------------  FORMULARIO USUARIOS ---------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
#
#
'''
-   Definimos los forms para Registrar, editar y agregar avatar a los usuarios.

'''


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
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'E-Mail', 'style': 'width: 250px;', 'class': 'form-control'}))
    password1 = forms.CharField(
        label="Ingrese Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'style': 'width: 200px;', 'class': 'form-control'}), error_messages={
            'required': 'Porfavor Ingresa La contraseña'
        })
    password2 = forms.CharField(
        label="Repita Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'style': 'width: 200px;', 'class': 'form-control'}), error_messages={
            'required': 'Porfavor Ingresa La contraseña'
        })
    first_name = forms.CharField(label='Modificar Nombre', error_messages={
        'required': 'Porfavor Ingresa tu nombre'
    }, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 200px;', 'class': 'form-control'}))
    last_name = forms.CharField(label='Modificar Apellido', error_messages={
        'required': 'Porfavor Ingresa Tu Apellido'
    }, widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'style': 'width: 200px;', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2',
                  'first_name', 'last_name']
        help_texts = {k: "" for k in fields}


# # Definimos el formulario para los Avatares:
class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")
