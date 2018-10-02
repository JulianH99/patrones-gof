from warrior import Warrior

# proxy
class LeveledWarrior(object):

    def __init__(self, level):
        self.__warrior = Warrior()

        if level < 10:
            self.__warrior.set_speed(10)
            self.__warrior.set_attack(10)
            self.__warrior.set_defense(10)
        elif level >= 10 and level < 20:
            self.__warrior.add_sword()
        elif level >= 20 and level < 30:
            self.__warrior.add_sword()
            self.__warrior.add_armor()
        elif level >= 30 and level <= 50:
            self.__warrior.add_sword()
            self.__warrior.add_armor()
            self.__warrior.add_boots()
        

    def fight(self):
        self.__warrior.fight()
    
    def defense(self):
        self.__warrior.defense()

    def move(self):
        self.__warrior.move()
        