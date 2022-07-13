from rve.controlador import IObservadorPantalla

class PantallaPrincipal(IObservadorPantalla.ObservadorPantalla):

    cantidadActualVisitantes = 0

    #Actualiza la cantidad de visitantes de la pantalla
    def actualizarCantidadVisitantes(self, cantidad):
        self.cantidadActualVisitantes = cantidad