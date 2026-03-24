print("__________________________________________")


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starting")

    def stop(self):
        print("Car stopping")


class Bicycle(Vehicle):
    def start(self):
        print("Bicycle starting")

    def stop(self):
        print("Bicycle stopping")


my = Car()
you = Bicycle()
my.start()
my.stop()
your.start()
your.stop()
