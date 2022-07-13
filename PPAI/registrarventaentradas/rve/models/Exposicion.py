from django.db import models
from .Empleado import Empleado
from .DetalleExposicion import DetalleExposicion

class Exposicion(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_fin = models.DateField()
    fecha_fin_replanificada = models.DateField()
    fecha_inicio = models.DateField()
    fecha_inicio_replanificada = models.DateField()
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, null=True)
    detalle = models.ForeignKey(DetalleExposicion, on_delete=models.PROTECT, null=True)
    sede_asignada = models.IntegerField(null=True)

    #MetodosClaseExposicion
    #Recibe como parametro el id de la exposicion
    #En la lista se guardan las duraciones de las obras
    #Ejecuta de la clase Detalle de Exposicion el metodo Buscar Duracion Obra
    def calcularDuracionObrasExpuestas(self, id):
        duracion = []
        detalles = DetalleExposicion.objects.filter(exposicion_asignada__icontains= id)
        for det in detalles:
            duracion.append(det.buscarDuracionObra())
        return sum(duracion)



    def esVigente(self, fecha_actual):
        if (self.fecha_fin.year > fecha_actual.year):
            return True
        elif ((self.fecha_fin.year == fecha_actual) and (self.fecha_fin.month > fecha_actual.month)):
            return True
        elif ((self.fecha_fin.year == fecha_actual) and (self.fecha_fin.month == fecha_actual.month) and (self.fecha_fin.day >= fecha_actual.day)):
            return True
        else:
            return False


