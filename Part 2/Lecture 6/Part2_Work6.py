class Person:
    def __init__(self):
        self.heart = Heart()
        self.brain = Brain()


class Heart:
    def __init__(self, usage=90):
        self.usage = usage

    @property
    def state(self):
        if self.usage > 70:
            return "high blood pressure"
        return "feeling good"


class Brain:
    def __init__(self, usage=60):
        self.usage = usage

    @property
    def state(self):
        if self.usage > 90:
            return "tired"
        return "rested"


class Leg:
    def __init__(self, moving_speed):
        self.mov_spd = moving_speed

    @property
    def moving_speed(self):
        if self.mov_spd > 10:
            return "running"
        elif self.mov_spd > 0:
            return "walking"
        return "standing"


person = Person()
person.leg = Leg(11)
print(person.heart.state)