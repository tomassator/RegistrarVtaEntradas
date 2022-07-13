from django.db import models
from .Empleado import Empleado

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    caducidad = models.DateField()
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, null=True) #Clave foranea

    #MetodosUsuario
    def conocerEmpleado(self):
        None

    #Devuelve el empleado asociado al usuario
    def obtenerEmpleado(self):
        return self.empleado


