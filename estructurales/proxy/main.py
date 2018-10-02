from leveled_warrior import LeveledWarrior
from random import randint

def main():
    rand = randint(1, 50)

    warrior = LeveledWarrior(rand)

    warrior.fight()
    warrior.defense()
    warrior.move()

if __name__ == '__main__':
    main()