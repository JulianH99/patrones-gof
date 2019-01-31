class Warrior(object):

    def __init__(self):
        self.__speed = 0
        self.__attack = 0
        self.__defense = 0
        self.__has_armor = False
        self.__has_sword = False
        self.__has_boots = False


    def set_speed(self, value):
        self.__speed = value

    
    def set_attack(self, value):
        self.__attack = value

    
    def set_defense(self, value):
        self.__defense = value

    def add_sword(self):
        self.__has_sword = True
        self.__attack += 20
    
    def add_armor(self):
        self.__has_armor = True
        self.__defense += 20

    def add_boots(self):
        self.__has_boots = True
        self.__speed += 20

    def fight(self):
        if self.__has_sword:
            message = "Take this sword attack!:"
        else:
            message = "Gonna punch you out:"

        print("{} {}".format(message, self.__attack))

    def defense(self):
        if(self.__has_armor):
            message = "Can't hit me man:"
        else:
            message = "ouch!:"
        
        print("{} {}".format(message, self.__defense))

    def move(self):
        if self.__has_boots:
            message = "I'm movin' so fast:"
        else:
            message = "Men, i'm so slow:"

        print("{} {}".format(message, self.__speed))

    
