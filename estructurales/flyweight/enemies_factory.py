from enemy_helper import EnemyTypes
from enemies import Zombie, Vampire

class EnemiesFactory:
    """ Generates enemies with different powers """

    def __init__(self):
        self._enemies = {}

    def get_enemy(self, enemy_type, power):
        """
            Gets an enemy by its type

            :type enemy_type: EnemyTypes
            :param enemy_type: Type of the enemy

            :type power: int
            :param power: power of the enemy

            :rtrntype: Enemy

        """
        try:
            enemy = self._enemies[enemy_type]
            enemy.set_power(power)
        except KeyError:
            if enemy_type == EnemyTypes.vampire:
                enemy = Vampire(power)
            elif enemy_type == EnemyTypes.zombie:
                enemy = Zombie(power)

            self._enemies[enemy_type] = enemy

        return enemy