from datetime import date
from django.db import models
from .Tarifa import Tarifa
from .Exposicion import Exposicion
from .Empleado import Empleado
import datetime

class Sede(models.Model):

    "Atributos de la clase Sede"
    cantMaximaVisitantes = models.IntegerField()
    cantMaxPorGuia = models.IntegerField()
    nombre = models.CharField(max_length=100)
    tarifas = models.ForeignKey(Tarifa, on_delete=models.PROTECT, null=True)
    exposicion = models.ForeignKey(Exposicion, on_delete=models.PROTECT, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, null=True)


    "Metodos de la clase Sede"

    #Metodos get
    def getCantMaximaVisitantes(self):
        return self.cantMaximaVisitantes

    def getCantMaxPorGuia(self):
        return self.cantMaxPorGuia

    def getNombre(self):
        return self.nombre


    #Metodos set
    def setCantMaximaVisitantes(self,cantMaximaVisitantes):
        self.cantMaximaVisitantes = cantMaximaVisitantes

    def setCantMaxPorGuia(self,cantMaxPorGuia):
        self.cantMaxPorGuia = cantMaxPorGuia

    def setNombre(self,nombre):
        self.nombre = nombre

    def conocerExposicion(self):
        None

    def buscarDuracionExposicion(self):
        None

    def buscarExposicion(self):
        None

    #Metodo que calcula la duracion aproximada de las exposiciones vigentes, En la lista se guardan los tiempos de las
    #obras de cada exposicion vigente. De cada exposicion vigente ejecuta el metodo calcularDuracionObrasExpuestas(exp.id)
    #Pasando por parametro el id de la exposicion
    def calcularDuracionExposicionVigentes(self,id, fecha_actual):
        duracion_exposiciones = []
        exposiciones_vigentes = Exposicion.objects.filter(sede_asignada__icontains=id)
        for exp in exposiciones_vigentes:
            if exp.esVigente(fecha_actual):
                duracion_exposiciones.append(exp.calcularDuracionObrasExpuestas(exp.id))    #Se crea una lista con los tiempos de cada exposicion
        return duracion_exposiciones


    #Metodo para filtrar las tarifas vigentes
    def obtenerTarifasVigentes(self, tarifas):
        tarifas_vigentes = []
        fActual = datetime.date.today()
        fActual = fActual.isoformat()

        #Año actual
        fActualYear = fActual[0] + fActual[1] + fActual[2] + fActual[3]
        fActualYear = int(fActualYear)

        #Mes actual
        fActualMonth = fActual[5] + fActual[6]
        fActualMonth = int(fActualMonth)

        #Mes actual
        fActualDia = fActual[8] + fActual[9]
        fActualDia = int(fActualDia)

        for tarifa in tarifas:
            #Tomando la fecha de fin de vigencia de la tarifa y convirtiendola de string a int
            fVigent = tarifa.getfechaFinVigencia()

            #Año tarifa
            fVigentYear = fVigent[0] + fVigent[1] + fVigent[2] + fVigent[3]
            fVigentYear = int(fVigentYear)

            #Mes tarifa
            fVigentMont = fVigent[5] + fVigent[6]
            fVigentMont = int(fVigentMont)

            #Día Tarifa.
            fVigentDia = fVigent[8] + fVigent[9]
            fVigentDia = int(fVigentDia)

            if fVigentYear > fActualYear:
                tarifas_vigentes.append(tarifa)
            elif fVigentYear == fActualYear:
                if fVigentMont > fActualMonth:
                    tarifas_vigentes.append(tarifa)
            elif fVigentMont == fActualMonth:
                if fVigentDia > fActualDia:
                    tarifas_vigentes.append(tarifa)
        return tarifas_vigentes  



