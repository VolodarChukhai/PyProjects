class Hero:
    def __init__(self, name, level, race):
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all parameters of this hero"""
        discription = (self.name + " Level is: " + str(self.level) + " Race is: "
                       + self.race + " Health is: " + str(self.health))
        print(discription)

    def level_up(self):
        self.level += 1

    def move(self):
        print("Hero " + self.name + " start moving")

    def set_health(self, new_health):
        self.health = new_health


class SuperHero(Hero):
    """Class to create super hero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our superhero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def make_magic(self):
        self.magic -= 10

    def show_hero(self):
        discription = (self.name + " Level is: " + str(self.level) + " Race is: "
                       + self.race + " Health is: " + str(self.health) + " Magic is: " + str(self.magic))
        print(discription)
