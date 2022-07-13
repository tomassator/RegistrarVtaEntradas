#Pantalla que actualiza la cantidad de visitantes de la sede
from rve.controlador import gestorVentaEntrada
from rve.controlador import IObservadorPantalla

class PantallaSede(IObservadorPantalla.ObservadorPantalla):

    nombre = ""
    cantidadActualVisitantes = 0

    #Actualiza la cantidad de visitantes de la pantalla
    def actualizarCantidadVisitantes(self, cantidad):
        self.cantidadActualVisitantes = cantidad

    def setNombre(self, nom):
        self.nombre = nom

    def getNombre(self):
        return self.nombre