from abc import ABC, abstractmethod

class AbsClass(ABC):

    @staticmethod
    def yardasABS(pies,metros):
        yardas = (metros * 1.094) + (pies / 3.281)
        return yardas

    @staticmethod
    def millasABS(pies,metros):
        millas = (metros * 1609) + (pies / 3.281)
        return millas

    @staticmethod
    def pulgadasABS(pies,metros):
        pulgadas = (metros * 39.37) + (pies / 3.281)
        return pulgadas

    @staticmethod
    def metrosABS(pies,metros):
        metros = metros + (pies / 3.281)
        return metros