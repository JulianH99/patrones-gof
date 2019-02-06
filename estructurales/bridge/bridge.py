import abc

class Switch(metaclass=abc.ABCMeta):
    def __init__(self, imp):
        self._imp = imp

    @abc.abstractmethod
    def On(self):
        pass

class WallLighter(Switch):
    def On(self):
        print('el boton esta activado')
        self._imp.switchOn()

class ElectricPulley(Switch):
    def On(self):
        print('la polea esta activada')
        self._imp.switchOn()

class SwitchItem(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def switchOn(self):
        pass

class Tv(SwitchItem):
    def switchOn(self):
        print('el televisor esta encendidio')

class ElectricDoor(SwitchItem):
    def switchOn(self):
        print('la puerta esta abriendo')

def main():
    puerta = ElectricDoor()
    television = Tv()
    polea = ElectricPulley(puerta)
    boton = WallLighter(television)

    polea.On()
    boton.On()


if __name__ == "__main__":
    main()