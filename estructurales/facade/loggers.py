from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum, auto, unique

@unique
class LoggerLevels(Enum):
    WARNING = auto()
    ERROR = auto()
    INFO = auto()


class Logger():
    __metaclass__ = ABC

    @abstractmethod
    def print_message(self, level, message):
        pass

    def log(self, level, message):
        if level in LoggerLevels:
            self.print_message(level.name, message)
        else:
            raise ValueError("{} is not a valid logging level".format(level))

    @staticmethod
    def _formated_message(level, message):
        return "[{}] - {}: {}".format(level, datetime.now(), message)


class ConsoleLogger(Logger):

    def print_message(self, level, message):
        print(ConsoleLogger._formated_message(level, message))


class HtmlLogger(Logger):

    def __init__(self, filename):
        Logger.__init__(self)
        self.__filename = filename

    def print_message(self, level, message):
        with open(self.__filename + '.html', 'a') as htmlfile:
            htmlfile.write("<b>{}<b><br>\n".format(
                self._formated_message(level, message)))
