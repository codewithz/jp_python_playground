import abc;

#abc --> Abstract Base Class

class Car(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

#-----------------------------------------------------

class HondaCity(Car):
    def start(self):
        print("Start 0f HC")

    def stop(self):
        print("Stop 0f HC")

h=HondaCity()