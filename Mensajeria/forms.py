from distutils.command.install_egg_info import to_filename
from email.policy import default
from msilib.schema import Control
from sys import maxsize
from tkinter import Widget
from tkinter.tix import Tree
from django import forms
from django.contrib.auth.models import User
from requests import request
from Mensajeria.models import *


####################################################################################################################################################
# -------------  FORMULARIO MENSAJE-----------------------------------------------------------------------------------------------------------------
####################################################################################################################################################
# # Definimos el formulario los mensajes:
class MensajeriaForm(forms.Form):

    mensajeForm = forms.CharField(
        max_length=500, label="Mensaje", widget=forms.Textarea(attrs={'cols': 80, 'rows': 10, 'placeholder': 'Escriba el Mensaje', 'class': 'form-control'}))
    usuarioDestinoForm = forms.ModelChoiceField(label="Destinatario",
                                                queryset=User.objects.all(), initial="", widget=forms.Select(attrs={'style': 'width: 150px;', 'class': 'form-control'}))
