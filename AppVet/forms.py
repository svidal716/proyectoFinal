from sys import maxsize
from tkinter import Widget
from django import forms


# Creamos el Formulario general para la primera entrega.

especieMascota = ["Perro", "Gato", "Otra"]
sexoMascota = ["Macho", "Hembra"]
vacunaMascota = ["Primovacunación", "Polivalente", "Ref Polivalente", "Rabia"]


class veterinariaFormulario(forms.Form):

    # creamos los campos del formulario:

    nombreVetForm = forms.CharField(max_length=40)
    apellidoVetForm = forms.CharField(max_length=40)
    fechaNacimientoVetForm = forms.DateField()
    matriculaVetForm = forms.IntegerField(max_length=10)
    emailVetForm = forms.EmailField()
    telefonoVetForm = forms.IntegerField()

    nombrePropietarioForm = forms.CharField(max_length=40)
    apellidoPropietarioForm = forms.CharField(max_length=40)
    fechaNacimientoPropietarioForm = forms.DateField()
    dniPropietarioForm = forms.ImageField(max_length=8)
    emailPropietarioForm = forms.EmailField()
    direccionPropietarioForm = forms.CharField(max_length=100)
    barrioPropietarioForm = forms.CharField(max_length=40)
    ciudadPropietarioForm = forms.CharField(max_length=40)
    telefonoPropietarioForm = forms.IntegerField()

    nombreMascotaForm = forms.CharField(max_length=40)
    razaMascotaForm = forms.CharField(max_length=40)
    especieMascotaForm = forms.ChoiceField(
        choices=especieMascota, required=True, label="Seleccione la Especie")

    echaNacimientoMascotaForm = forms.DateField()

    fechaConsultaForm = forms.DateField()
    # -------- Lista con Macho / Hembra
    sexoMascotaForm = forms.ChoiceField(
        choices=sexoMascota, required=True, label="Seleccione el Sexo")
    pesoMascotaForm = forms.FloatField(maxsize=5)
    colorMascotaForm = forms.CharField(max_length=20)
    enfermedadPreviaMascotaForm = forms.CharField(max_length=100)
    # -------- Checkbox con las vacunas.
    vacunasMascotasForm = forms.CheckboxSelectMultiple(
        Widget=forms.CheckboxSelectMultiple, choices=vacunaMascota)

    # -------- Lista (Balanceado / Varios )
    comidaMascotaForm = forms.CharField(max_length=40)
    temperaturaMascotaForm = forms.FloatField(maxsize=5)
    motivoConsultaForm = forms.CharField(max_length=400)
    diagnosticoMascotaForm = forms.CharField(max_length=400)
    # -----> Seleccionar de la lista de Veterinarios Agregados.
    veterinarioMascotaForm = forms.CharField(max_length=80)
