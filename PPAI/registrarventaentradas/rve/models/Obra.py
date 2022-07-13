from django.db import models
from .Empleado import Empleado

class Obra(models.Model):
    "Atributos de la clase Obra"
    alto = models.IntegerField()
    ancho = models.IntegerField()
    codigoSensor = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    duracionExtendida = models.IntegerField()  #La duracion extendida se expresa en minutos
    duracionResumida = models.IntegerField()    #La duracion resumida se expresa en minutos
    fechaCreacion = models.DateField()
    fechaPrimerIngreso = models.DateField()
    nombreObra = models.CharField(max_length=100)
    peso = models.IntegerField()
    valuacion = models.CharField(max_length=100)
    empleados = models.ForeignKey(Empleado, on_delete=models.PROTECT, null=True)

    "Metodos de la clase Obra"

    "Metodos get"
    def getAlto(self):
        return self.alto

    def getAncho(self):
        return self.ancho

    def getCodigo(self):
        return self.codigoSensor

    def getDescripcion(self):
        return self.descripcion

    def getDuracionExtendida(self):
        return self.duracionExtendida

    #Devuelve la duracion resumida
    def getDuracionResumida(self):
        return self.duracionResumida

    def getFechaCreacion(self):
        return self.fechaCreacion

    def getFechaPrimerIngreso(self):
        return self.fechaPrimerIngreso

    def getNombreObra(self):
        return self.nombreObra

    def getPeso(self):
        return self.peso

    def getValuacion(self):
        return self.valuacion

    "metodos set"
    def setAlto(self,alto):
        self.alto = alto

    def setAncho(self,ancho):
        self.ancho = ancho

    def setCodigoSensor(self,codigoSensor):
        self.codigoSensor

    def setDescripcion(self,descripcion):
        self.descripcion = descripcion

    def setDuracionExtendida(self,duracionExtendida):
        self.duracionExtendida = duracionExtendida

    def setDuracionResumida(self,duracionResumida):
        self.duracionResumida = duracionResumida

    def setFechaCreacion(self,fechaCreacion):
        self.fechaCreacion = fechaCreacion

    def setFechaPrimerIngreso(self,fechaPrimerIngreso):
        self.fechaPrimerIngreso = fechaPrimerIngreso

    def setNombreObra(self,nombreObra):
        self.nombreObra = nombreObra

    def setPeso(self,peso):
        self.peso = peso

    def setValuacion(self,valuacion):
        self.valuacion

    "Metodo conocer"
    def conocerEmpleado(self):
        None
