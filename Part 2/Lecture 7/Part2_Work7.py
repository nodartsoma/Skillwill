from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, max_speed=240, current_speed=0):
        self.max_speed = max_speed
        self.current_speed = current_speed

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        return "car stopped"


class SportCar(Car):
    def start_engine(self):
        print(super().start_engine())
        return Car().max_speed

    def stop_engine(self):
        print(super().stop_engine())
        Car().current_speed = 0

