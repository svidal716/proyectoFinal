from django.urls import path
from AppVet import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path('veterinarios/', views.veterinarios, name="veterinarios"),
    path('propietarios/', views.propietarios, name="propietarios"),
    path('mascotas/', views.mascotas, name="mascotas"),
    path('historiaClinica/', views.historiaClinica, name="historiaClinica"),
    path('busquedaVeterinario/', views.busquedaVeterinario,
         name="busquedaVeterinario"),
    path('buscar/', views.buscar, name="buscar")

]
