from django.urls import path
from AppVet import views


urlpatterns = [
    path('AppVet/ ', views.inicio, name="index"),
    path('veterinarios/', views.veterinarios, name="veterinarios"),

]
