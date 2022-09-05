<h1 align="center"> Doctor Vet </h1>



![Esta es una imagen](https://i2.wp.com/zoovetesmipasion.com/wp-content/uploads/2017/10/veterinario-.jpg?fit=712%2C350)



* Descripcion del Proyecto
  
  El desarrollo de la web que hicimos esta basada en mantener un historial de las mascotas que son atendidas en las diferentes veterinarias, poder consultar todos los  datos y el historial medico, asi el veterinario puede conocer y administrar la correcta medicina



* Requerimientos

  Definimos los siguientes modelos para poder obtener los datos de los veterinarios, dueños de mascotas y mascotas:
  - datosVeterinarios
  - datosPropietario
  - datosMascota
  - historiaClinica

* Guia de uso:

- En primer lugar nos dirigimos a la url principal: http://127.0.0.1:8000/AppVet/ 
 
![inicio](https://user-images.githubusercontent.com/97696225/188517023-082653c5-dc47-4d41-b646-3275a4a2d425.PNG)


- Luego podemos navegar por el menu de la pagina principal:

![menu](https://user-images.githubusercontent.com/97696225/188517262-28c36340-6d47-4182-8e49-ffc4f4960434.png)

para el cual se crearon las siguientes URLs:

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

- En cada seccion de nuestra Web podremos completar los formularios correspondientes para agregar la informacion a la base de datos. Como por ejemplo en la seccion  
http://127.0.0.1:8000/AppVet/veterinarios/ se podran cargar los datos de los distintos veterinarios.

![ejemploVeterinarios](https://user-images.githubusercontent.com/97696225/188517569-af2d5dfc-9a42-489c-a8fe-0c44dc129531.png)

- Una vez enviado los datos quedaran guardados en la DB.

![db](https://user-images.githubusercontent.com/97696225/188517668-fda3cb1e-8c1a-4ba7-8a09-a653b5f7b8a7.png)



