from abc import ABC,abstractmethod
from typing import List
from Model.Observer import Observer
class Subject(ABC):
    def __init__(self):
        self.observers=[]

    def add_observer(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self,observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notify_observers(self,update_type,data=None):
        for observer in self.observers:
            observer.update(update_type,data)

    def get_obs_list(self)->List[Observer]:
        return self.observers

    def set_obs_list(self,obs_list:List[Observer]):
        self.observers=obs_list.copy()