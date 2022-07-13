from django.db import models
from .Usuario import Usuario

class Sesion(models.Model):
    fecha_fin = models.DateField(null=True)
    fecha_inicio = models.DateField()
    hora_fin = models.TimeField(null=True)
    hora_inicio = models.TimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True) #Clave foranea


    #MetodosSesion

    #Retorna el usuario asociado a la sesion
    def conocerUsuario(self):
        return self.usuario

    #Metodo que llama a usuario para obtener el empleado asociado al usuario
    def getEmpleadoEnSesion(self):
        empleado = self.usuario.obtenerEmpleado()
        return empleado
