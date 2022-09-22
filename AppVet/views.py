from django.shortcuts import render
from AppVet.models import *
from django.http import HttpResponse
from AppVet.forms import *
from AppVet.choice import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

# Creamos las vistas del MENU:


def index(request):

    return render(request, "AppVet/index.html")


def about(request):

    return render(request, "AppVet/about.html")


def services(request):

    return render(request, "AppVet/services.html")


def contact(request):

    return render(request, "AppVet/contact.html")


# Creamos las Vistas para  Administracion

@login_required
def appAdmin(request):

    return render(request, "AppVet/App/app_admin.html")


####################################################################################################################################################
# -------------  LOGIN -----------------------------------------------------------------------------------------------------------------------------
####################################################################################################################################################


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = request.POST["username"]
            passwd = request.POST["password"]

            usuario = authenticate(username=user, password=passwd)

            if usuario is not None:

                login(request, usuario)
                return render(request, 'AppVet/App/app_admin.html', {'mensaje': f"Bienvenido {usuario}"})
            else:
                return render(request, "AppVet/App/login.html", {"formulario": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppVet/App/login.html", {"formulario": form, "mensaje": "Usuario o contraseña incorrectos"})

    else:
        form = AuthenticationForm()
        return render(request, "AppVet/App/login.html", {"formulario": form})


# Creamos la View para iniciar sesion:


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, "AppVet/App/login.html", {"mensaje": f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppVet/App/Usuario/registrar_usr.html", {"formulario": form, "mensaje": "FORMULARIO INVALIDO"})

    else:
        form = UserRegisterForm()
        return render(request, "AppVet/App/Usuario/registrar_usr.html", {"formulario": form})


# @login_required
# def editarPerfil(request):
#     usuario = request.user
#     if request.method == "POST":
#         form = UserEditForm(request.POST)
#         if form.is_valid():
#             info = form.cleaned_data
#             usuario.email = info["email"]
#             usuario.password1 = info["password1"]
#             usuario.password2 = info["password2"]
#             usuario.first_name = info["first_name"]
#             usuario.last_name = info["last_name"]
#             usuario.save()
#             return render(request, "AppCoder/inicio.html", {"mensaje": "Perfil editado correctamente"})
#         else:
#             return render(request, "AppCoder/editarPerfil.html", {"formulario": form, "usuario": usuario, "mensaje": "FORMULARIO INVALIDO"})
#     else:
#         form = UserEditForm(instance=usuario)
#     return render(request, "AppCoder/editarPerfil.html", {"formulario": form, "usuario": usuario, "avatar": obtenerAvatar(request)})


# @login_required
# def agregarAvatar(request):
#     if request.method == 'POST':
#         formulario = AvatarForm(request.POST, request.FILES)
#         if formulario.is_valid():
#             avatarViejo = Avatar.objects.filter(user=request.user)
#             if(len(avatarViejo) > 0):
#                 avatarViejo[0].delete()
#             avatar = Avatar(user=request.user,
#                             imagen=formulario.cleaned_data['imagen'])
#             avatar.save()
#             return render(request, 'AppCoder/inicio.html', {'usuario': request.user, 'mensaje': 'AVATAR AGREGADO EXITOSAMENTE', "avatar": avatar.imagen.url})
#         else:
#             return render(request, 'AppCoder/agregarAvatar.html', {'formulario': formulario, 'mensaje': 'FORMULARIO INVALIDO'})

#     else:
#         formulario = AvatarForm()
#         return render(request, "AppCoder/agregarAvatar.html", {"formulario": formulario, "usuario": request.user, "avatar": obtenerAvatar(request)})


# def obtenerAvatar(request):
#     lista = Avatar.objects.filter(user=request.user)
#     if len(lista) != 0:
#         imagen = lista[0].imagen.url
#     else:
#         imagen = "/media/avatares/avatarpordefecto.png"
#     return imagen
####################################################################################################################################################
# -------------   VETERINARIO  ---------------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# Inicio Veterinarios


def inicioVete(request):

    return render(request, "AppVet/App/Veterinario/inicio_veterinario.html")

# Agregar Veterinario a la DB.


@login_required
def agregarVeterinarios(request):

    if request.method == "POST":

        formularioVet = veterinarioForm(request.POST)

        if formularioVet.is_valid():

            info = formularioVet.cleaned_data

        # Guardamos la data del form en la DB

            veterinario = DatosVeterinarios(nombreVet=info["nombreVetForm"], apellidoVet=info["apellidoVetForm"],
                                            matriculaVet=info["matriculaVetForm"], emailVet=info["emailVetForm"],
                                            fechaNacimientoVet=info["fechaNacimientoVetForm"], telefonoVet=info["telefonoVetForm"])

            veterinario.save()

            return render(request, "AppVet/App/app_admin.html", {"mensaje": "Vete Creado"})
    else:

        formularioVet = veterinarioForm()
        return render(request, "AppVet/App/Veterinario/agregar_veterinario.html", {"formularioVet": formularioVet})


'''
Vamos a tener dos Vistas diferentes:
    1 - Una donde esta el formulario donde pongo a buscar
    2 - Otra donde me muestre el resultado.  (buscar)
    (Se pueden hacer ambas juntas)

'''
# Buscamos Veterinario a la DB.


@login_required
def busquedaVeterinario(request):
    # me va a mostrar un formulario.

    return render(request, "AppVet/App/Veterinario/buscar_veterinario.html")


@login_required
def buscarVeterinario(request):

    if request.GET["veterinario"]:

        veterinarios = request.GET["veterinario"]
        busquedaVete = DatosVeterinarios.objects.filter(
            nombreVet=veterinarios)  # Filtramos por nombre de Veterinario

        return render(request, "AppVet/App/Veterinario/resultado_busqueda_veterinario.html", {"busquedaVete": busquedaVete})

    else:
        return render(request, "AppVet/App/Veterinario/resultado_busqueda_veterinario.html", {"mensaje": "Ingresa un Nombre de Veterinario"})


@login_required
def busquedaVeteAll(request):

    veterinarios = DatosVeterinarios.objects.all()

    return render(request, "AppVet/App/Veterinario/busqueda_veterinarioall.html", {"veterinarios": veterinarios})
# Eliminamos Veterinario:


@login_required
def eliminarVeterinario(request, id):

    veterinario = DatosVeterinarios.objects.get(id=id)
    veterinario.delete()

    return render(request, "AppVet/App/Veterinario/eliminar_veterinario.html")


# Modificamos Datos del Veterinario:
@login_required
def modificarVeterinario(request, id):

    veterinario = DatosVeterinarios.objects.get(id=id)

    if request.method == "POST":

        formularioVetMod = veterinarioForm(request.POST)

        if formularioVetMod.is_valid():

            info = formularioVetMod.cleaned_data
            veterinario.nombreVet = info["nombreVetForm"]
            veterinario.apellidoVet = info["apellidoVetForm"]
            veterinario.matriculaVet = info["matriculaVetForm"]
            veterinario.emailVet = info["emailVetForm"]
            veterinario.fechaNacimientoVet = info["fechaNacimientoVetForm"]
            veterinario.telefonoVet = info["telefonoVetForm"]

            veterinario.save()
            veterinarios = DatosVeterinarios.objects.all()

            return render(request, "AppVet/App/Veterinario/busqueda_veterinarioall.html", {"veterinarios": veterinarios})

    else:
        formularioVetMod = veterinarioForm(initial={"nombreVetForm": veterinario.nombreVet, "apellidoVetForm": veterinario.apellidoVet,
                                                    "matriculaVetForm": veterinario.matriculaVet, "emailVetForm": veterinario.emailVet,
                                                    "fechaNacimientoVetForm": veterinario.fechaNacimientoVet, "telefonoVetForm": veterinario.telefonoVet})

        return render(request, "AppVet/App/Veterinario/modificar_veterinario.html", {"formularioVetMod": formularioVetMod, "veterinario": veterinario})


####################################################################################################################################################
# -------------   PROPIETARIO MASCOTA   ------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
@login_required
def inicioPropietario(request):

    return render(request, "AppVet/App/Propietario/inicio_propietario.html")


# Definimos el Model Datos Dueño de la Mascota:
@login_required
def agregarPropietario(request):

    if request.method == "POST":

        formularioProp = propietarioForm(request.POST)

        if formularioProp.is_valid():

            info = formularioProp.cleaned_data

        # Guardamos la data del form en la DB

            propietario = DatosPropietario(nombrePropietario=info["nombrePropietarioForm"],
                                           apellidoPropietario=info["apellidoPropietarioForm"],
                                           fechaNacimientoPropietario=info["fechaNacimientoPropietarioForm"],
                                           dniPropietario=info["dniPropietarioForm"],
                                           emailPropietario=info["emailPropietarioForm"],
                                           direccionPropietario=info["direccionPropietarioForm"],
                                           barrioPropietario=info["barrioPropietarioForm"],
                                           ciudadPropietario=info["ciudadPropietarioForm"],
                                           telefonoPropietario=info["telefonoPropietarioForm"])

            propietario.save()

            return render(request, "AppVet/App/Propietario/inicio_propietario.html", {"mensaje": "Propietario Creado"})
    else:

        formularioProp = propietarioForm()
        return render(request, "AppVet/App/Propietario/agregar_propietario.html", {"formularioProp": formularioProp})

# Buscamos PROPIETARIO a la DB.


@login_required
def busquedaPropietario(request):
    # me va a mostrar un formulario.

    return render(request, "AppVet/App/Propietario/buscar_propietario.html")


@login_required
def buscarPropietario(request):

    if request.GET["propietario"]:

        propietario = request.GET["propietario"]
        busquedaPropietario = DatosPropietario.objects.filter(
            nombrePropietario=propietario)  # Filtramos por nombre de Propietario

        return render(request, "AppVet/App/Propietario/resultado_busqueda_propietario.html", {"busquedaPropietario": busquedaPropietario})

    else:
        return render(request, "AppVet/App/Propietario/resultado_busqueda_propietario.html", {"mensaje": "Ingresa un Nombre de Veterinario"})


@login_required
def busquedaPropAll(request):

    propietarios = DatosPropietario.objects.all()

    return render(request, "AppVet/App/Propietario/busqueda_propietario_all.html", {"propietarios": propietarios})

# Eliminamos Propietario:


@login_required
def eliminarPropietario(request, id):

    propietario = DatosPropietario.objects.get(id=id)
    propietario.delete()

    return render(request, "AppVet/App/Propietario/eliminar_propietario.html")


# Modificamos Datos del propietario:
@login_required
def modificarPropietario(request, id):

    propietario = DatosPropietario.objects.get(id=id)

    if request.method == "POST":

        formularioPropMod = propietarioForm(request.POST)

        if formularioPropMod.is_valid():

            info = formularioPropMod.cleaned_data
            propietario.nombrePropietario = info["nombrePropietarioForm"]
            propietario.apellidoPropietario = info["apellidoPropietarioForm"]
            propietario.fechaNacimientoPropietario = info["fechaNacimientoPropietarioForm"]
            propietario.dniPropietario = info["dniPropietarioForm"]
            propietario.emailPropietario = info["emailPropietarioForm"]
            propietario.direccionPropietario = info["direccionPropietarioForm"]
            propietario.barrioPropietario = info["barrioPropietarioForm"]
            propietario.ciudadPropietario = info["ciudadPropietarioForm"]
            propietario.telefonoPropietario = info["telefonoPropietarioForm"]

            propietario.save()
            propietarios = DatosPropietario.objects.all()

            return render(request, "AppVet/App/Propietario/busqueda_propietario_all.html", {"propietarios": propietarios})

    else:
        formularioPropMod = propietarioForm(initial={"nombrePropietarioForm": propietario.nombrePropietario,
                                                     "apellidoPropietarioForm": propietario.apellidoPropietario,
                                                     "fechaNacimientoPropietarioForm": propietario.fechaNacimientoPropietario,
                                                     "dniPropietarioForm": propietario.dniPropietario,
                                                     "emailPropietarioForm": propietario.emailPropietario,
                                                     "direccionPropietarioForm": propietario.direccionPropietario,
                                                     "barrioPropietarioForm": propietario.barrioPropietario,
                                                     "ciudadPropietarioForm": propietario.ciudadPropietario,
                                                     "telefonoPropietarioForm": propietario.telefonoPropietario})

        return render(request, "AppVet/App/Propietario/modificar_propietario.html", {"formularioPropMod": formularioPropMod, "propietario": propietario})


####################################################################################################################################################
# -------------  DATOS  MASCOTA         ------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el Model Datos principales de la Mascota:

@login_required
def inicioMascota(request):

    return render(request, "AppVet/App/Mascota/inicio_mascota.html")


@login_required
def agregarMascota(request):

    if request.method == "POST":

        formularioMascotas = mascotaForm(request.POST)

        if formularioMascotas.is_valid():

            info = formularioMascotas.cleaned_data

        # Guardamos la data del form en la DB

            mascota = DatosMascota(nombreMascota=info["nombreMascotaForm"],
                                   razaMascota=info["razaMascotaForm"],
                                   especieMascota=info["especieMascotaForm"],
                                   fechaNacimientoMascota=info["fechaNacimientoMascotaForm"])

            mascota.save()

            return render(request, "AppVet/App/Mascota/inicio_mascota.html", {"mensaje": "Macota Creada"})
    else:
        formularioMascotas = mascotaForm()
        return render(request, "AppVet/App/Mascota/agregar_mascota.html", {"formularioMascotas": formularioMascotas})


# Buscamos PROPIETARIO a la DB.

@login_required
def busquedaMascota(request):
    # me va a mostrar un formulario.

    return render(request, "AppVet/App/Mascota/buscar_mascota.html")


@login_required
def buscarMascota(request):

    if request.GET["mascota"]:

        mascota = request.GET["mascota"]
        busquedaMascota = DatosMascota.objects.filter(
            nombreMascota=mascota)  # Filtramos por nombre de Propietario

        return render(request, "AppVet/App/Mascota/resultado_busqueda_mascota.html", {"busquedaMascota": busquedaMascota})

    else:
        return render(request, "AppVet/App/Mascota/resultado_busqueda_mascota.html", {"mensaje": "Ingresa el Nombre de la Mascota:"})


@login_required
def busquedaMascotaAll(request):

    mascotas = DatosMascota.objects.all()

    return render(request, "AppVet/App/Mascota/busqueda_mascota_all.html", {"mascotas": mascotas})

# Eliminamos Mascota:


@login_required
def eliminarMascota(request, id):

    mascota = DatosMascota.objects.get(id=id)
    mascota.delete()

    return render(request, "AppVet/App/Mascota/eliminar_mascota.html")


# Modificamos Datos del propietario:
@login_required
def modificarMascota(request, id):

    mascota = DatosMascota.objects.get(id=id)

    if request.method == "POST":

        formularioMascotaMod = mascotaForm(request.POST)

        if formularioMascotaMod.is_valid():

            info = formularioMascotaMod.cleaned_data
            mascota.nombreMascota = info["nombreMascotaForm"],
            mascota.razaMascota = info["razaMascotaForm"],
            mascota.especieMascota = info["especieMascotaForm"],
            mascota.fechaNacimientoMascota = info["fechaNacimientoMascotaForm"]

            mascota.save()
            mascotas = DatosMascota.objects.all()

            return render(request, "AppVet/App/Mascota/busqueda_mascota_all.html", {"mascotas": mascotas})

    else:
        formularioMascotaMod = mascotaForm(initial={"nombreMascotaForm":   mascota.nombreMascota,
                                                    "razaMascotaForm":  mascota.razaMascota,
                                                    "especieMascotaForm": mascota.especieMascota,
                                                    "fechaNacimientoMascotaForm": mascota.fechaNacimientoMascota
                                                    })

        return render(request, "AppVet/App/Mascota/modificar_mascota.html", {"formularioMascotaMod": formularioMascotaMod, "mascota": mascota})


####################################################################################################################################################
# -------------   HISTORIA CLINICA MASCOTA   -------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# Inicio Historia Clinica
