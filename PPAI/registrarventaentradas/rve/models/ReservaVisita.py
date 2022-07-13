from django.db import models
from .Sede import Sede

class ReservaVisita(models.Model):
    cantidadAlumnos = models.IntegerField()
    cantidadAlumnosConfirmada = models.IntegerField()
    duracionEstimada = models.IntegerField()
    fechaHoraCreacion = models.DateTimeField()
    fechaHoraReserva = models.DateTimeField()
    horaFinReal = models.IntegerField()
    horaInicioReal = models.IntegerField()
    numeroReserva = models.IntegerField()
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT, null=True)


    #Metodos GET
    def getCantidadAlumnos(self):
        return self.cantidadAlumnos

    def getCantidadAlumnosConfirmada(self):
        return self.cantidadAlumnosConfirmada

    def getDuracionEstimada(self):
        return self.duracionEstimada

    def getFechaHoraCreacion(self):
        return self.fechaHoraCreacion

    def getFechaHoraReserva(self):
        return self.fechaHoraReserva

    def getHoraFinReal(self):
        return self.getHoraFinReal

    def getHoraInicioReal(self):
        return self.horaInicioReal

    def getNumeroReserva(self):
        return self.numeroReserva

    #Metodos SET
    def setCantidadAlumnos(self,cantidadAlumnos):
        self.cantidadAlumnos = cantidadAlumnos

    def setCantidadAlumnosConfirmada(self,cantidadAlumnosConfirmada):
        self.cantidadAlumnosConfirmada = cantidadAlumnosConfirmada

    def setDuracionEstimada(self,duracionEstimada):
        self.duracionEstimada = duracionEstimada

    def setFechaHoraCreacion(self,fechaHoraCreacion):
        self.fechaHoraCreacion = fechaHoraCreacion

    def setFechaHoraReserva(self,fechaHoraReserva):
        self.fechaHoraReserva = fechaHoraReserva

    def setHoraFinReal(self,horaFinReal):
        self.getHoraFinReal = horaFinReal

    def setHoraInicioReal(self,horaInicioReal):
        self.horaInicioReal = horaInicioReal

    def setNumeroReserva(self,numeroReserva):
        self.numeroReserva = numeroReserva


    #Valida si la reserva esta en el rango de horario de la venta de la entrada
    def sonParaFechaYHoraYSede(self, fechaActual):
        if self.fechaHoraReserva.year == fechaActual.year and self.fechaHoraReserva.month == fechaActual.month and self.fechaHoraReserva.day == fechaActual.day:
            if (self.horaInicioReal <= fechaActual.hour and self.horaFinReal >= fechaActual.hour):
                return True
        return False
