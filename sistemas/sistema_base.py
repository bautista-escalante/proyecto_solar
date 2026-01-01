from abc import ABC, abstractmethod

class Sistema_base(ABC):

    @abstractmethod
    def calcular_paneles(self):
        pass

    @abstractmethod
    def calcular_baterias(self):
        pass

    @abstractmethod
    def calcular_inversor(self):
        pass
