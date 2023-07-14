from abc import ABC,abstractmethod

class Computer(ABC):
    
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):

    def laptop(self):
        print("proccessing process 1")

class Mobile(Laptop):

    def mobile(self):
        print("processing mobile")

    def process(self):
        print("proceesing")

#com = Computer()
# lap = Laptop()
# lap.laptop()
mob = Mobile()
mob.laptop()
mob.mobile()
mob.process()