class DatosMascota(models.Model):

    nombreMascota = models.CharField(max_length=30)
    razaMascota = models.CharField(max_length=50)
    # ----------------------------modificar lista
    especieMascota = models.CharField(max_length=30)
    fechaNacimientoMascota = models.DateField()
    apellidoPropietarioMascota = models.ForeignKey(
        DatosPropietario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombreMascota+" "+str(self.razaMascota)+" "+str(self.especieMascota)+" "+str(self.fechaNacimientoMascota)+" "+str(self.apellidoPropietarioMascota)
# Definimos el Model historia Clinica de la Mascota.
