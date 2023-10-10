
class Car:
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
    def change_color(self, new_color):
        if not isinstance(new_color, str):
            return "Please, insert string"
        elif new_color != Car.color:
            self.__color = new_color
            return True
        else:
            return False

    @property
    def horse_power(self):
        return self.__horse_power

    @horse_power.setter
    def increase_horse_power(self, hp):
        if not isinstance(hp, int):
            return "Please, insert integer"
        elif hp > 0:
            self.__horse_power += hp
            return True
        else:
            return False

    @property
    def is_sport_car(self):
        return self.__is_sport_car

