from django.urls import path
from django.contrib.auth.views import LogoutView
from AppVet import views


urlpatterns = [

    # -------------- URL GENERALES ---------------------------

    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    #path('inicio/', views.inicio, name="inicio"),


    # -------------- URL APP ADMINISTRACION-------------------------

    path('app_admin/', views.appAdmin, name="appAdmin"),
    path('login/', views.login_request, name="Login"),


    # -------------- URL VETERINARIO ---------------------------

    path('agregarVeterinarios/', views.agregarVeterinarios,
         name="agregarVeterinarios"),
    path('busquedaVeterinario/', views.busquedaVeterinario,
         name="busquedaVeterinario"),
    path('buscarVeterinario/', views.buscarVeterinario, name="buscarVeterinario"),
    path('inicioVete/', views.inicioVete, name="inicioVete"),
    path('eliminarVeterinario/<id>', views.eliminarVeterinario,
         name="eliminarVeterinario"),
    path('busquedaVeteAll/', views.busquedaVeteAll, name="busquedaVeteAll"),
    path('modificarVeterinario/<id>', views.modificarVeterinario,
         name="modificarVeterinario"),

    # -------------- URL PROPIETARIOS ---------------------------

    path('inicioPropietario/', views.inicioPropietario, name="inicioPropietario"),
    path('agregarPropietario/', views.agregarPropietario,
         name="agregarPropietario"),

    path('busquedaPropietario/', views.busquedaPropietario,
         name="busquedaPropietario"),
    path('buscarPropietario/', views.buscarPropietario, name="buscarPropietario"),

    path('eliminarPropietario/<id>', views.eliminarPropietario,
         name="eliminarPropietario"),
    path('busquedaPropAll/', views.busquedaPropAll, name="busquedaPropAll"),

    path('modificarPropietario/<id>', views.modificarPropietario,
         name="modificarPropietario"),

    # -------------- URL MASCOTAS --------------------------------

    path('inicioMascota/', views.inicioMascota, name="inicioMascota"),
    path('agregarMascota/', views.agregarMascota,
         name="agregarMascota"),

    path('busquedaMascota/', views.busquedaMascota,
         name="busquedaMascota"),
    path('buscarMascota/', views.buscarMascota, name="buscarMascota"),

    path('eliminarMascota/<id>', views.eliminarMascota,
         name="eliminarMascota"),
    path('busquedaMascotaAll/', views.busquedaMascotaAll,
         name="busquedaMascotaAll"),

    path('modificarMascota/<id>', views.modificarMascota,
         name="modificarMascota"),


    # -------------- URL HISTORIA CLINICA ---------------------------

    path('inicioClinica/', views.inicioClinica, name="inicioClinica"),
    path('agregarClinica/', views.agregarClinica,
         name="agregarClinica"),

    #     path('busquedaMascota/', views.busquedaMascota,
    #          name="busquedaMascota"),
    #     path('buscarMascota/', views.buscarMascota, name="buscarMascota"),

    #     path('busquedaMascotaAll/', views.busquedaMascotaAll,
    #          name="busquedaMascotaAll"),

    #     path('modificarMascota/<id>', views.modificarMascota,
    #          name="modificarMascota"),


    # login register logout
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppVet/App/Usuario/logout.html'), name='logout'),
    path('agregarAvatar/', views.agregarAvatar, name='agregarAvatar'),
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'),


]
