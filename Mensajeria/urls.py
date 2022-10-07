from django.urls import path
from django.contrib.auth.views import LogoutView
from Mensajeria import views


urlpatterns = [

    # -------------- URL GENERALES ---------------------------

    path("inicioMsj/", views.inicioMsj, name="inicioMsj"),
    path("mensajes/", views.mensajes, name="mensajes"),
    path("responder/", views.responder, name="responder"),


]
