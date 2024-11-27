from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self,update_type,data=None):
        """
        Metoda care este apelată când subiectul notifică observatorul cu schimbări.
        """
        pass
