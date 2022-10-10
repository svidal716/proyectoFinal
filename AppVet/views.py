from django.shortcuts import render
from psutil import users
from AppVet.models import *
from django.http import HttpResponse
from AppVet.forms import *
from AppVet.choices import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


######################################################################################################################################
#
#
# Creamos las vistas para el Menu principal de la web:


def index(request):

    return render(request, "AppVet/index.html")


def about(request):

    return render(request, "AppVet/about.html")


def services(request):

    return render(request, "AppVet/services.html")


###################################################################################################################################################
# -------------  LOGIN ----------------------------------------------------------------------------------------------------------------------------
###################################################################################################################################################
#
#
# Creamos las vistas relacionadas con Iniciar Sesion, Registrar nuevo Usuario, Editar usuario, Agregar Avatar:


@login_required
def appAdmin(request):

    return render(request, "AppVet/App/app_admin.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = request.POST["username"]
            passwd = request.POST["password"]

            usuario = authenticate(username=user, password=passwd)

            if usuario is not None:

                login(request, usuario)
                return render(request, 'AppVet/App/app_admin.html', {"username": obtenerUser(request), 'mensaje': f"Bienvenido {usuario}", "avatar": obtenerAvatar(request)})
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


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()
            return render(request, 'AppVet/App/app_admin.html', {"username": {usuario}, "mensaje": "Perfil editado correctamente"})
        else:
            return render(request, 'AppVet/App/Usuario/editar_usuario.html', {"username": obtenerUser(request), "formulario": form, "usuario": usuario, "mensaje": "FORMULARIO INVALIDO", "avatar": obtenerAvatar(request)})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, 'AppVet/App/Usuario/editar_usuario.html', {"username": obtenerUser(request), "formulario": form, "usuario": usuario, "avatar": obtenerAvatar(request)})


@ login_required
def agregarAvatar(request):
    if request.method == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo = Avatar.objects.filter(user=request.user)
            if(len(avatarViejo) > 0):
                avatarViejo[0].delete()
            avatar = Avatar(user=request.user,
                            imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'AppVet/App/app_admin.html', {"username": obtenerUser(request), 'mensaje': 'AVATAR AGREGADO EXITOSAMENTE', "avatar": avatar.imagen.url})
        else:
            return render(request, 'AppVet/App/Usuario/agregar_avatar.html', {"username": obtenerUser(request), 'formulario': formulario, 'mensaje': 'FORMULARIO INVALIDO'})

    else:
        formulario = AvatarForm()
        return render(request, 'AppVet/App/Usuario/agregar_avatar.html', {"username": obtenerUser(request), "formulario": formulario, "usuario": request.user, "avatar": obtenerAvatar(request)})


@ login_required
def obtenerAvatar(request):
    lista = Avatar.objects.filter(user=request.user)
    if len(lista) != 0:
        imagen = lista[0].imagen.url
    else:
        imagen = "/media/avatares/avatarpordefecto.png"
    return imagen


@ login_required
def obtenerUser(request):
    username = request.user.username
    return username

# Inicio Creadores


@ login_required
def inicioCreadores(request):

    return render(request, "AppVet/App/creadores.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})


####################################################################################################################################################
# -------------   VETERINARIO  ---------------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# Inicio Veterinarios

@ login_required
def inicioVete(request):

    return render(request, "AppVet/App/Veterinario/inicio_veterinario.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})

# Agregar Veterinario nuevo Veterinario.


@ login_required
def agregarVeterinarios(request):

    if request.method == "POST":

        formularioVet = VeterinarioForm(request.POST)

        if formularioVet.is_valid():

            info = formularioVet.cleaned_data

            veterinario = DatosVeterinarios(nombreVet=info["nombreVetForm"], apellidoVet=info["apellidoVetForm"],
                                            matriculaVet=info["matriculaVetForm"], emailVet=info["emailVetForm"],
                                            fechaNacimientoVet=info["fechaNacimientoVetForm"], telefonoVet=info["telefonoVetForm"])

            veterinario.save()

            return render(request, "AppVet/App/app_admin.html", {"username": obtenerUser(request), "mensaje": "Vete Creado", "avatar": obtenerAvatar(request)})
    else:

        formularioVet = VeterinarioForm()
        return render(request, "AppVet/App/Veterinario/agregar_veterinario.html", {"username": obtenerUser(request), "formularioVet": formularioVet, "avatar": obtenerAvatar(request)})


# Buscamos Veterinario a la DB.
@ login_required
def busquedaVeterinario(request):

    return render(request, "AppVet/App/Veterinario/buscar_veterinario.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})


@ login_required
def buscarVeterinario(request):

    if request.GET["veterinario"]:

        veterinarios = request.GET["veterinario"]
        busquedaVete = DatosVeterinarios.objects.filter(
            nombreVet=veterinarios)

        return render(request, "AppVet/App/Veterinario/resultado_busqueda_veterinario.html", {"username": obtenerUser(request), "busquedaVete": busquedaVete, "avatar": obtenerAvatar(request)})

    else:
        return render(request, "AppVet/App/Veterinario/resultado_busqueda_veterinario.html", {"username": obtenerUser(request), "mensaje": "Ingresa un Nombre de Veterinario", "avatar": obtenerAvatar(request)})


@ login_required
def busquedaVeteAll(request):

    veterinarios = DatosVeterinarios.objects.all()

    return render(request, "AppVet/App/Veterinario/busqueda_veterinarioall.html", {"username": obtenerUser(request), "veterinarios": veterinarios, "avatar": obtenerAvatar(request)})


# Eliminamos Veterinario:
@ login_required
def eliminarVeterinario(request, id):

    veterinario = DatosVeterinarios.objects.get(id=id)
    veterinario.delete()

    return render(request, "AppVet/App/Veterinario/eliminar_veterinario.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})


# Modificamos Datos del Veterinario:
@ login_required
def modificarVeterinario(request, id):

    veterinario = DatosVeterinarios.objects.get(id=id)

    if request.method == "POST":

        formularioVetMod = VeterinarioForm(request.POST)

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

            return render(request, "AppVet/App/Veterinario/busqueda_veterinarioall.html", {"username": obtenerUser(request), "veterinarios": veterinarios, "avatar": obtenerAvatar(request)})

    else:
        formularioVetMod = VeterinarioForm(initial={"nombreVetForm": veterinario.nombreVet, "apellidoVetForm": veterinario.apellidoVet,
                                                    "matriculaVetForm": veterinario.matriculaVet, "emailVetForm": veterinario.emailVet,
                                                    "fechaNacimientoVetForm": veterinario.fechaNacimientoVet, "telefonoVetForm": veterinario.telefonoVet})

        return render(request, "AppVet/App/Veterinario/modificar_veterinario.html", {"username": obtenerUser(request), "formularioVetMod": formularioVetMod, "veterinario": veterinario, "avatar": obtenerAvatar(request)})


####################################################################################################################################################
# -------------   PROPIETARIO MASCOTA   ------------------------------------------------------------------------------------------------------------
####################################################################################################################################################

# Inicio Propietario / Cliente
@ login_required
def inicioPropietario(request):

    return render(request, "AppVet/App/Propietario/inicio_propietario.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})


# Agregamos Cliente:
@ login_required
def agregarPropietario(request):

    if request.method == "POST":

        formularioProp = PropietarioForm(request.POST)

        if formularioProp.is_valid():

            info = formularioProp.cleaned_data

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

            return render(request, "AppVet/App/Propietario/inicio_propietario.html", {"username": obtenerUser(request), "mensaje": "Cliente Agregado.", "avatar": obtenerAvatar(request)})
    else:

        formularioProp = PropietarioForm()
        return render(request, "AppVet/App/Propietario/agregar_propietario.html", {"username": obtenerUser(request), "formularioProp": formularioProp, "avatar": obtenerAvatar(request)})

# Buscamos Clientes.


@ login_required
def busquedaPropietario(request):

    return render(request, "AppVet/App/Propietario/buscar_propietario.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})


@ login_required
def buscarPropietario(request):

    if request.GET["propietario"]:

        propietario = request.GET["propietario"]
        busquedaPropietario = DatosPropietario.objects.filter(
            nombrePropietario=propietario)

        return render(request, "AppVet/App/Propietario/resultado_busqueda_propietario.html", {"username": obtenerUser(request), "busquedaPropietario": busquedaPropietario, "avatar": obtenerAvatar(request)})

    else:
        return render(request, "AppVet/App/Propietario/resultado_busqueda_propietario.html", {"username": obtenerUser(request), "mensaje": "Ingresa un Nombre de Veterinario", "avatar": obtenerAvatar(request)})


@ login_required
def busquedaPropAll(request):

    propietarios = DatosPropietario.objects.all()

    return render(request, "AppVet/App/Propietario/busqueda_propietario_all.html", {"username": obtenerUser(request), "propietarios": propietarios, "avatar": obtenerAvatar(request)})

# Eliminamos Propietario:


@ login_required
def eliminarPropietario(request, id):

    propietario = DatosPropietario.objects.get(id=id)
    propietario.delete()

    return render(request, "AppVet/App/Propietario/eliminar_propietario.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})


# Modificamos Datos del propietario:
@ login_required
def modificarPropietario(request, id):

    propietario = DatosPropietario.objects.get(id=id)

    if request.method == "POST":

        formularioPropMod = PropietarioForm(request.POST)

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

            return render(request, "AppVet/App/Propietario/busqueda_propietario_all.html", {"username": obtenerUser(request), "propietarios": propietarios, "avatar": obtenerAvatar(request)})

    else:
        formularioPropMod = PropietarioForm(initial={"nombrePropietarioForm": propietario.nombrePropietario,
                                                     "apellidoPropietarioForm": propietario.apellidoPropietario,
                                                     "fechaNacimientoPropietarioForm": propietario.fechaNacimientoPropietario,
                                                     "dniPropietarioForm": propietario.dniPropietario,
                                                     "emailPropietarioForm": propietario.emailPropietario,
                                                     "direccionPropietarioForm": propietario.direccionPropietario,
                                                     "barrioPropietarioForm": propietario.barrioPropietario,
                                                     "ciudadPropietarioForm": propietario.ciudadPropietario,
                                                     "telefonoPropietarioForm": propietario.telefonoPropietario})

        return render(request, "AppVet/App/Propietario/modificar_propietario.html", {"username": obtenerUser(request), "formularioPropMod": formularioPropMod, "propietario": propietario, "avatar": obtenerAvatar(request)})


####################################################################################################################################################
# -------------  DATOS  MASCOTA         ------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# Inicio Mascotas
@ login_required
def inicioMascota(request):

    return render(request, "AppVet/App/Mascota/inicio_mascota.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})

# Agregamos nueva mascota


@ login_required
def agregarMascota(request):

    if request.method == "POST":

        formularioMascotas = MascotaForm(request.POST, request.FILES)

        if formularioMascotas.is_valid():

            info = formularioMascotas.cleaned_data

            mascota = DatosMascota(nombreMascota=info["nombreMascotaForm"],
                                   razaMascota=info["razaMascotaForm"],
                                   especieMascota=info["especieMascotaForm"],
                                   fechaNacimientoMascota=info["fechaNacimientoMascotaForm"],
                                   apellidoPropietarioMascota=info["apellidoPropietarioMascotaForm"])

            mascota.save()

            return render(request, "AppVet/App/Mascota/inicio_mascota.html", {"username": obtenerUser(request), "mensaje": "Macota Creada", "avatar": obtenerAvatar(request)})
    else:
        formularioMascotas = MascotaForm()
        return render(request, "AppVet/App/Mascota/agregar_mascota.html", {"username": obtenerUser(request), "formularioMascotas": formularioMascotas, "avatar": obtenerAvatar(request)})


# Buscamos Mascota.

@ login_required
def busquedaMascota(request):

    return render(request, "AppVet/App/Mascota/buscar_mascota.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})


@ login_required
def buscarMascota(request):

    if request.GET["mascota"]:

        mascota = request.GET["mascota"]
        busquedaMascota = DatosMascota.objects.filter(
            nombreMascota=mascota)  # Filtramos por nombre de Mascota

        return render(request, "AppVet/App/Mascota/resultado_busqueda_mascota.html", {"username": obtenerUser(request), "busquedaMascota": busquedaMascota, "avatar": obtenerAvatar(request)})

    else:
        return render(request, "AppVet/App/Mascota/resultado_busqueda_mascota.html", {"username": obtenerUser(request), "mensaje": "Ingresa el Nombre de la Mascota:", "avatar": obtenerAvatar(request)})


@ login_required
def busquedaMascotaAll(request):

    mascotas = DatosMascota.objects.all()

    return render(request, "AppVet/App/Mascota/busqueda_mascota_all.html", {"username": obtenerUser(request), "mascotas": mascotas, "avatar": obtenerAvatar(request)})

# Eliminamos Mascota:


@ login_required
def eliminarMascota(request, id):

    mascota = DatosMascota.objects.get(id=id)
    mascota.delete()

    return render(request, "AppVet/App/Mascota/eliminar_mascota.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})


# Modificamos Datos de la Mascota:
@ login_required
def modificarMascota(request, id):

    mascota = DatosMascota.objects.get(id=id)

    if request.method == "POST":

        formularioMascotaMod = MascotaForm(request.POST)

        if formularioMascotaMod.is_valid():

            info = formularioMascotaMod.cleaned_data
            mascota.nombreMascota = info["nombreMascotaForm"],
            mascota.razaMascota = info["razaMascotaForm"],
            mascota.especieMascota = info["especieMascotaForm"],
            mascota.fechaNacimientoMascota = info["fechaNacimientoMascotaForm"]
            mascota.apellidoPropietarioMascota = info["apellidoPropietarioMascotaForm"]

            mascota.save()
            mascotas = DatosMascota.objects.all()

            return render(request, "AppVet/App/Mascota/busqueda_mascota_all.html", {"username": obtenerUser(request), "mascotas": mascotas, "avatar": obtenerAvatar(request)})

    else:
        formularioMascotaMod = MascotaForm(initial={"nombreMascotaForm":   mascota.nombreMascota,
                                                    "razaMascotaForm":  mascota.razaMascota,
                                                    "especieMascotaForm": mascota.especieMascota,
                                                    "fechaNacimientoMascotaForm": mascota.fechaNacimientoMascota,
                                                    "apellidoPropietarioMascotaForm": mascota.apellidoPropietarioMascota
                                                    })

        return render(request, "AppVet/App/Mascota/modificar_mascota.html", {"username": obtenerUser(request), "formularioMascotaMod": formularioMascotaMod, "mascota": mascota, "avatar": obtenerAvatar(request)})


####################################################################################################################################################
# -------------   HISTORIA CLINICA MASCOTA   -------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# Inicio Historia Clinica


@ login_required
def inicioClinica(request):

    return render(request, "AppVet/App/Mascota/hclinica/inicio_hclinica.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})

# Agregamos nueva historia Clinica


@ login_required
def agregarClinica(request):

    if request.method == "POST":

        formularioHClinica = HistoriaClinicaForm(request.POST)

        if formularioHClinica.is_valid():

            info = formularioHClinica.cleaned_data

            historiaClinica = HistoriaClinica(fechaConsulta=info["fechaConsultaForm"],
                                              nombreMascota=info["nombreMascotaForm"],
                                              sexoMascota=info["sexoMascotaForm"],
                                              pesoMascota=info["pesoMascotaForm"],
                                              enfermedadPreviaMascota=info["enfermedadPreviaMascotaForm"],
                                              vacunasMascotas=info["vacunasMascotasForm"],
                                              comidaMascota=info["comidaMascotaForm"],
                                              temperaturaMascota=info["temperaturaMascotaForm"],
                                              motivoConsulta=info["motivoConsultaForm"],
                                              diagnosticoMascota=info["diagnosticoMascotaForm"],
                                              veterinarioMascota=info["veterinarioMascotaForm"])

            historiaClinica.save()

            return render(request, "AppVet/App/Mascota/hclinica/inicio_hclinica.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})
    else:
        formularioHClinica = HistoriaClinicaForm()
        return render(request, "AppVet/App/Mascota/hclinica/agregar_hclinica.html", {"formularioHClinica": formularioHClinica, "username": obtenerUser(request), "avatar": obtenerAvatar(request)})


# Buscamos Historia Clinica
@ login_required
def busquedaClinica(request):
    # me va a mostrar un formulario.

    return render(request, "AppVet/App/Mascota/hclinica/buscar_hclinica.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})


@ login_required
def buscarClinica(request):

    if request.GET["mascota"]:

        hclinica = request.GET["mascota"]
        busquedaHistoriaClinica = HistoriaClinica.objects.filter(
            nombreMascota=hclinica)  # Filtramos por nombre de la Mascota

        return render(request, "AppVet/App/Mascota/hclinica/resultado_busqueda_hclinica.html", {"username": obtenerUser(request), "busquedaHistoriaClinica": busquedaHistoriaClinica, "avatar": obtenerAvatar(request)})

    else:
        return render(request, "AppVet/App/Mascota/hclinica/resultado_busqueda_hclinica.html", {"username": obtenerUser(request), "mensaje": "Ingresa el Nombre de la Mascota:", "avatar": obtenerAvatar(request)})


@ login_required
def busquedaClinicaAll(request):

    hclinica = HistoriaClinica.objects.all()

    return render(request, "AppVet/App/Mascota/hclinica/busqueda_hclinica_all.html", {"username": obtenerUser(request), "hclinica": hclinica, "avatar": obtenerAvatar(request)})

# Eliminamos Historia Clinica:


@ login_required
def eliminarClinica(request, id):

    clinica = HistoriaClinica.objects.get(id=id)
    clinica.delete()

    return render(request, "AppVet/App/Mascota/hclinica/eliminar_hclinica.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})
