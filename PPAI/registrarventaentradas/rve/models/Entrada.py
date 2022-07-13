from django.db import models

from .Sede import Sede
from .Tarifa import Tarifa
from datetime import datetime, time


class Entrada(models.Model):

    #Atributos
    fechaVenta = models.DateTimeField(null=True)
    horaVenta = models.IntegerField()
    monto = models.IntegerField()
    numero = models.IntegerField()
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT, null=True)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.PROTECT, null=True)
    
    #Metodos

    def getfechaVenta(self):
        return self.fechaVenta 
    
    def gethoraVenta(self):
        return self.horaVenta

    def getmonto(self):
        return self.horaVenta
    
    def getnumero(self):
        return self.numero

    def getsede(self):
        return self.sede
    
    def gettarifa(self):
        return self.tarifa

    def setfechaVenta(self,x):
        self.fechaVenta = x

    def sethoraVenta(self,x):
        self.horaVenta = x

    def setmonto(self,x):
        self.monto = x
    
    def setnumero(self,x):
        self.numero = x

    def conocerGuiaAsignado(self):
        None

    #Valida si hay entradas vendidas en el rango de horario para la venta actual
    def sonDeFechaHoraSede(self, fechaActual):
        if ((self.fechaVenta.year == fechaActual.year) and (self.fechaVenta.month == fechaActual.month) and (self.fechaVenta.day == fechaActual.day)):
            if (self.fechaVenta.hour == fechaActual.hour) or (self.fechaVenta.hour >= (fechaActual.hour - 1)):
                return True
        return False
