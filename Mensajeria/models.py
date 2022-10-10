from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from traitlets import default


# Creamos los models para el sistema de mensajeria:


# Definimos y le damos formato a la fecha y hora, para luego guardarlas automaticamente.
def get_default_my_hour():
    hour = timezone.now()
    formatedHour = hour.strftime("%H:%M:%S")
    return formatedHour


class Mensajeria(models.Model):
    day = timezone.now()
    formatedDay = day.strftime("%d/%m/%Y")
    fechaMensaje = models.CharField(max_length=50, default=formatedDay)
    horaMensaje = models.CharField(max_length=50, default=get_default_my_hour)
    usuarioDestino = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="UsuarioDestino")
    usuarioOrigen = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="UsuarioOrigen")
    mensaje = models.CharField(max_length=500)

    def __str__(self):
        return self.usuarioDestino
