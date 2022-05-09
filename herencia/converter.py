from abc import ABCMeta
from abc import ABC
from abc import abstractmethod

class Convertidor(metaclass=ABCMeta):

    @abstractmethod
    def convert(self, value):
        pass

    @abstractmethod
    def getResult(self):
        pass

class AbstractConvertidor(ABC, Convertidor):
    _result = float(0)

    def getResult(self):
        return self._result


class MetrosConvertidor(AbstractConvertidor):

    def __init__(self, pies, metros):
        self._result = self.convert(pies) + metros

    def convert(self, value):
        return value / 3.281


class MillasConvertidor(AbstractConvertidor):

    def __init__(self, pies, metros):
        self._result = self.convert(metros) + self.convert(MetrosConvertidor(pies, 0).getResult())

    def convert(self, value):
        return value * 1609


class PulgadasConvertidor(AbstractConvertidor):

    def __init__(self, pies, metros):
        self._result = self.convert(metros) + self.convert(MetrosConvertidor(pies, 0).getResult())

    def convert(self, value):
        return value * 39.37


class YardasConvertidor(AbstractConvertidor):

    def __init__(self, pies, metros):
        self._result = self.convert(metros) + self.convert(MetrosConvertidor(pies, 0).getResult())

    def convert(self, value):
        return value * 1.094