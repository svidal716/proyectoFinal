from django.shortcuts import render
from AppVet.models import *
from django.http import HttpResponse
from AppVet.forms import *
from AppVet.choice import *


# Create your views here.


def inicio(request):
    return render(request, "AppVet/inicio.html")

# Creamos la Views para Ingresar un nuevo Veterinario.


def veterinarios(request):

    if request.method == "POST":

        formularioVet = veterinarioForm(request.POST)

        if formularioVet.is_valid():

            info = formularioVet.cleaned_data

        # Guardamos la data del form en la DB

            veterinario = datosVeterinarios(nombreVet=info["nombreVetForm"], apellidoVet=info["apellidoVetForm"],
                                            matriculaVet=info["matriculaVetForm"], emailVet=info["emailVetForm"],
                                            fechaNacimientoVet=info["fechaNacimientoVetForm"], telefonoVet=info["telefonoVetForm"])

            veterinario.save()

            return render(request, "AppVet/inicio.html", {"mensaje": "Vete Creado"})
    else:

        formularioVet = veterinarioForm()
        return render(request, "AppVet/veterinarios.html", {"formularioVet": formularioVet})


# Definimos el Model Datos Dueño de la Mascota:


def propietarios(request):

    if request.method == "POST":

        formularioProp = propietarioForm(request.POST)

        if formularioProp.is_valid():

            info = formularioProp.cleaned_data

        # Guardamos la data del form en la DB

            propietario = datosPropietario(nombrePropietario=info["nombrePropietarioForm"],
                                           apellidoPropietario=info["apellidoPropietarioForm"],
                                           fechaNacimientoPropietario=info["fechaNacimientoPropietarioForm"],
                                           dniPropietario=info["dniPropietarioForm"],
                                           emailPropietario=info["emailPropietarioForm"],
                                           direccionPropietario=info["direccionPropietarioForm"],
                                           barrioPropietario=info["barrioPropietarioForm"],
                                           ciudadPropietario=info["ciudadPropietarioForm"],
                                           telefonoPropietario=info["telefonoPropietarioForm"])

            propietario.save()

            return render(request, "AppVet/inicio.html", {"mensaje": "Propietario Creado"})
    else:

        formularioProp = propietarioForm()
        return render(request, "AppVet/propietarios.html", {"formularioProp": formularioProp})


# # Definimos el Model Datos principales de la Mascota:

def mascotas(request):

    if request.method == "POST":

        formularioMascotas = mascotaForm(request.POST)

        if formularioMascotas.is_valid():

            info = formularioMascotas.cleaned_data

        # Guardamos la data del form en la DB

            mascota = datosMascota(nombreMascota=info["nombreMascotaForm"],
                                   razaMascota=info["razaMascotaForm"],
                                   especieMascota=info["especieMascotaForm"],
                                   fechaNacimientoMascota=info["fechaNacimientoMascotaForm"])

            mascota.save()

            return render(request, "AppVet/inicio.html", {"mensaje": "Macota Creada"})
    else:
        formularioMascotas = mascotaForm()
        return render(request, "AppVet/mascotas.html", {"formularioMascotas": formularioMascotas})


# Definimos el Model historia Clinica de la Mascota.
def historiaClinica(request):

    if request.method == "POST":

        formularioHisClinica = historiaForm(request.POST)

        if formularioHisClinica.is_valid():

            info = formularioHisClinica.cleaned_data

            hisClinica = historiaClinica(fechaConsulta=info["fechaConsultaForm"],
                                         sexoMascota=info["sexoMascotaForm"],
                                         pesoMascota=info["pesoMascotaForm"],
                                         colorMascota=info["colorMascotaForm"],
                                         enfermedadPreviaMascota=info["enfermedadPreviaMascotaForm"],
                                         vacunasMascotas=info["vacunasMascotasForm"],
                                         comidaMascota=info["comidaMascotaForm"],
                                         temperaturaMascota=info["temperaturaMascotaForm"],
                                         motivoConsulta=info["motivoConsultaForm"],
                                         diagnosticoMascota=info["diagnosticoMascotaForm"],
                                         veterinarioMascota=info["veterinarioMascotaForm"])

            hisClinica.save()
        return render(request, "AppVet/inicio.html", {"mensaje": "Hitoria Clinica Guardada"})

        # Guardamos la data del form en la DB

    else:
        formularioHisClinica = historiaForm()
        return render(request, "AppVet/historiaClinica.html", {"formularioHisClinica": formularioHisClinica})


# -------------- BUSQUEDAS ------------------------------------------------------------------------------------------

'''
Vamos a tener dos Vistas diferentes: 
    1 - Una donde esta el formulario donde pongo a buscar 
    2 - Otra donde me muestre el resultado.  (buscar)
    (Se pueden hacer ambas juntas)
    
'''


def busquedaVeterinario(request):
    # me va a mostrar un formulario.

    return render(request, "AppVet/busquedaVeterinario.html")


def buscar(request):

    if request.GET["veterinario"]:

        veterinarios = request.GET["veterinario"]

        # Traeme de la base de datos TODOS los veterinarios que tengan ese nombre.

        busquedaVete = datosVeterinarios.objects.filter(nombreVet=veterinarios)

        return render(request, "AppVet/resultadoBusqueda.html", {"busquedaVete": busquedaVete})

    else:
        return render(request, "AppVet/busquedaVeterinario.html", {"mensaje": "Ingresa un Nombre de Veterinario"})
