from django.db import models
from .Obra import Obra

class DetalleExposicion(models.Model):
    
    lugar_asignado = models.CharField(max_length=100)
    obra = models.ForeignKey(Obra, on_delete=models.PROTECT, null=True) #Clave Foranea
    exposicion_asignada = models.IntegerField(null=True)

    #MetodosDetalleExposicion

    # Ejecuta de OBRA el metodo getDuracionResumida
    def buscarDuracionObra(self):
        duracion = self.obra.getDuracionResumida()
        return duracion
    def conocerObra(self):
        None

    def conocerPared(self):
        None
