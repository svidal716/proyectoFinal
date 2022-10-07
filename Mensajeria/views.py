from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from AppVet.views import obtenerUser, obtenerAvatar
from Mensajeria.forms import *
from Mensajeria.models import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.


@login_required
def inicioMsj(request):

    usuario = request.user
    busquedaMensaje = Mensajeria.objects.filter(
        usuarioDestino=usuario)  # Filtramos por nombre de Veterinario

    return render(request, "Mensajeria/resultadoBusqueda.html", {"username": obtenerUser(request), "busquedaMensaje": busquedaMensaje, "avatar": obtenerAvatar(request)})


@login_required
def mensajes(request):
    if request.method == "POST":
        formularioMensaje = MensajeriaForm(request.POST)
        if formularioMensaje.is_valid():

            info = formularioMensaje.cleaned_data
            usuario = request.user
            Mensajeria.usuarioOrigen = usuario
            mensaje = Mensajeria(mensaje=info['mensajeForm'],
                                 usuarioDestino=info['usuarioDestinoForm'])
            mensaje.save()
            return render(request, "Mensajeria/mensajes.html", {"username": obtenerUser(request), "mensaje": "Vete Creado"}, {"avatar": obtenerAvatar(request)})
    else:
        formularioMensaje = MensajeriaForm()
        return render(request, "Mensajeria/mensajes.html", {"username": obtenerUser(request), "formularioMensaje": formularioMensaje, "avatar": obtenerAvatar(request)})


def responder(request):
    return render(request, "Mensajeria/responder.html", {"username": obtenerUser(request), "avatar": obtenerAvatar(request)})
