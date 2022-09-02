from django.shortcuts import render
from AppVet.models import *
from django.http import HttpResponse
from AppVet.forms import *

# Create your views here.


def inicio(request):

    return render(request, "AppVet/index.html")


def veterinarios(request):

    if request.method == "POST":

        form = veterinarioForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            nombreVet = info["nombreVetForm"]
            apellidoVet = info["apellidoVetForm"]
            matriculaVet = info["matriculaVetForm"]
            emailVet = info["emailVetForm"]
            telefonoVet = info["telefonoVetForm"]

            veterinario = datosVeterinarios(nombreVetForm=nombreVet, apellidoVetForm=apellidoVet,
                                            emailVetForm=emailVet, matriculaVetForm=matriculaVet, telefonoVetForm=telefonoVet)
            veterinario.save()

            return render(request, "AppVet/index.html", {"mensaje": "Vete Creado"})
    else:
        form = veterinarioForm()

    return render(request, "AppVet/pagina2.html", {"formulario": form})

# Definimos el Model Datos Dueño de la Mascota:


# def propietario(self):

#     return ("Vista Propietario")
# # Definimos el Model Datos principales de la Mascota:


# def mascota(self):

#     return ("Vista mascota")
# # Definimos el Model historia Clinica de la Mascota.


# def historiaClinica(self):

#     return ("Vista Historia")
