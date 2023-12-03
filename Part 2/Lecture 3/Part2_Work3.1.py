
class Car:
    champion = 1990

    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def production_year(self):
        return self.__production_year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        if not isinstance(new_color, str):
            print("Please, insert string")
        elif new_color != Car.color:
            self.__color = new_color

    @property
    def horse_power(self):
        return self.__horse_power

    @horse_power.setter
    def horse_power(self, hp):
        if not isinstance(hp, int):
            print("Please, insert integer")
        elif hp > 0:
            self.__horse_power += hp

    @property
    def is_sport_car(self):
        return self.__is_sport_car

    def show(self):
        print(f"name: {self.model}")




car = Car("BMW", "M4", 2010, "Black", 200, True)


