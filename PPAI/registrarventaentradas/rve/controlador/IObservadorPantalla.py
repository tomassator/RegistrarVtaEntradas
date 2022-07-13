from abc import ABCMeta
from abc import abstractmethod

class ObservadorPantalla(metaclass=ABCMeta):
    @abstractmethod
    def actualizarCantidadVisitantes(self, cantidad):
        pass
