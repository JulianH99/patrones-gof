from enemies_factory import EnemiesFactory
from enemy_helper import EnemyTypes
from random import choice, randint
from sys import argv

enemies_factory = EnemiesFactory()

def get_random_enemy(power):
    types = [EnemyTypes.vampire, EnemyTypes.zombie]
    selected_type = choice(types)

    return enemies_factory.get_enemy(selected_type, power)


def main():
    enemies = []

    print(argv[1])
    number_of_enemies = int(argv[1])

    if number_of_enemies == None:
        number_of_enemies = randint(1, 20)
    
    for x in range(number_of_enemies):
        power = randint(0, 100)
        enemies.append(get_random_enemy(power))

    for enemy in enemies:
        enemy.attack()



if __name__ == "__main__":
    main()