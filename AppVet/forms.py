from sys import maxsize
from tkinter import Widget
from django import forms


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
    emailVetForm = forms.EmailField(label="E-Mail Veterinario")
    telefonoVetForm = forms.IntegerField(label="Telefono Veterinario")


# class propietarioForm(forms.Form):

#     nombrePropietarioForm = forms.CharField(max_length=40)
#     apellidoPropietarioForm = forms.CharField(max_length=40)
#     fechaNacimientoPropietarioForm = forms.DateField()
#     dniPropietarioForm = forms.IntegerField()
#     emailPropietarioForm = forms.EmailField()
#     direccionPropietarioForm = forms.CharField(max_length=100)
#     barrioPropietarioForm = forms.CharField(max_length=40)
#     ciudadPropietarioForm = forms.CharField(max_length=40)
#     telefonoPropietarioForm = forms.IntegerField()


# class mascotaForm(forms.Form):

#     nombreMascotaForm = forms.CharField(max_length=40)
#     razaMascotaForm = forms.CharField(max_length=40)
#     especieMascotaForm = forms.ChoiceField(
#         choices=especieMascota, required=True, label="Seleccione la Especie")
#     echaNacimientoMascotaForm = forms.DateField()


# class historiaForm(forms.Form):

#     fechaConsultaForm = forms.DateField()
#     # -------- Lista con Macho / Hembra
#     # sexoMascotaForm = forms.ChoiceField(
#     #     choices=sexoMascota, required=True, label="Seleccione el Sexo")

#     pesoMascotaForm = forms.FloatField()
#     colorMascotaForm = forms.CharField(max_length=20)
#     enfermedadPreviaMascotaForm = forms.CharField(max_length=100)
#     # -------- Checkbox con las vacunas.

#     vacunasMascotasForm = forms.CheckboxSelectMultiple(
#         Widget=forms.CheckboxSelectMultiple, choices=vacunaMascota)

#     # -------- Lista (Balanceado / Varios )
#     comidaMascotaForm = forms.CharField(max_length=40)
#     temperaturaMascotaForm = forms.FloatField()
#     motivoConsultaForm = forms.CharField(max_length=400)
#     diagnosticoMascotaForm = forms.CharField(max_length=400)
#     # -----> Seleccionar de la lista de Veterinarios Agregados.
#     veterinarioMascotaForm = forms.CharField(max_length=80)
