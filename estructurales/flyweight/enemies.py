from abc import ABCMeta, abstractmethod


class Enemy(metaclass=ABCMeta):
    
    """ Represents an enemy of the hero """
    
    def __init__(self, power):
        """ 
        Initializes the enemy
        :type power: int
        :param power: power of the enemy


        :rtype: None
        """
        self._power = power
        self._name = None

    def attack(self):
        print("{} is attacking with power of {}".format(self._name, self._power))

    def set_power(self, power):
    
        """ Changes the power of the enemy
   
        :type power: int
        :param power: power of the enemy

        """    
        self._power = power


class Vampire(Enemy):

    """ Vampire enemy representation """

    def __init__(self, power):
        Enemy.__init__(self, power)
        self._name = 'Vampire'

class Zombie(Enemy):

    """ Zombie enemy representation """

    def __init__(self, power):
        Enemy.__init__(self, power)
        self._name = 'Zombie'
