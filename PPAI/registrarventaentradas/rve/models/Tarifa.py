from django.db import models

from .TipoEntrada import TipoEntrada
from .TipoVisita import TipoVisita


class Tarifa(models.Model):

    #Atributos de la clase Tarifa
    fechaFinVigencia = models.CharField(max_length=100)
    fechaInicioVigencia= models.CharField(max_length=100)
    monto = models.IntegerField()
    montoAdicionalGuia = models.IntegerField()
    nro_sede = models.IntegerField(null=True)
    tipoDeEntrada = models.ForeignKey(TipoEntrada, on_delete=models.PROTECT, null=True) #Clave foranea
    tipoVisita = models.ForeignKey(TipoVisita, on_delete=models.PROTECT, null=True) #Clave foranea

    #Metodos
    def new(self):
        return

    #Retorna el atributo
    def getfechaFinVigencia(self):
        return self.fechaFinVigencia

    # Retorna el atributo
    def getfechaIncioVigencia(self):
        return self.fechaInicioVigencia

    # Retorna el atributo
    def getmonto(self):
        return self.monto

    # Retorna el atributo
    def getmontoAdicionalGuia(self):
        return self.montoAdicionalGuia

    # Retorna el atributo
    def getTipoEntrada(self):
        return self.tipoDeEntrada

    # Retorna el atributo
    def getTipoVisita(self):
        return self.tipoVisita

    # Setea el atributo
    def setfechaFinVigencia(self, x):
        self.fechaFinVigencia = x

    # Setea el atributo
    def fechaInicioVigencia(self,x):
        self.fechaInicioVigencia = x

    # Setea el atributo
    def setmonto(self,x):
        self.monto = x

    # Setea el atributo
    def setmontoAdicionalGuia(self,x): 
        self.montoAdicionalGuia = x

    # Metodo que retorna el monto vigente de la tarifa
    def mostrarMontosVigentes(self):
        monto = self.getmonto()
        return monto


    
    
