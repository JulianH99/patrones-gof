import abc


class Arma(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def disparar(self):
        pass

class Decorador(Arma,metaclass=abc.ABCMeta):
    def __init__(self, arma):
        self._arma = arma
    @abc.abstractmethod
    def disparar(self):
        pass

class ArmaConGranada(Decorador):
    def disparar(self):
        print('boom')
        self._arma.disparar()

class ArmaConFuego(Decorador):
    def disparar(self):
        print('flushhhhh')
        self._arma.disparar()

class Ak_47(Arma):
    def disparar(self):
        print('piupiu')


def main():
    myArma = Ak_47()
    arma_granada = ArmaConGranada(myArma)
    arma_granada2 = ArmaConGranada(arma_granada)
    arma_granada2.disparar()


if __name__ == "__main__":
    main()