from abc import ABCMeta
from abc import abstractmethod


class sujestorPantalla(metaclass=ABCMeta):
    @abstractmethod
    def subscribir(IObservadorPantalla):
        pass

    @abstractmethod
    def quitar(IObservadorPantalla):
        pass

    @abstractmethod
    def notificar(self):
        pass
