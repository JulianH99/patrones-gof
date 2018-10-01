from abc import ABC, abstractmethod
from numbers_module import Numbers


class AbstractNumbersList(ABC):

    @abstractmethod
    def ten_first_evens(self):
        pass

    @abstractmethod
    def ten_first_odds(self):
        pass


class NumbersList(AbstractNumbersList):

    def __init__(self):
        self.__numbers = Numbers()

    def ten_first_evens(self):
        return self.__numbers.get_even_numbers(10)

    def ten_first_odds(self):
        return self.__numbers.get_odd_numbers(10)
