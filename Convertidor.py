class convertidor:
    __yardas = float(0)
    __metros = float(0)
    __millas = float(0)
    __pulgadas = float(0)

    #Metodo constructor
    def __init__(self, metros, pies):
        #Se realizará la sumatoria de todos los métodos
        piesConvertidos = pies / 3.281
        self.__metros = metros + piesConvertidos
        self.__convertirMetrosPulgadas(metros)
        self.__convertirMetrosPulgadas(piesConvertidos)
        self.__convertirMetrosYardas(metros)
        self.__convertirMetrosYardas(piesConvertidos)
        self.__convertirMetrosMillas(metros)
        self.__convertirMetrosMillas(piesConvertidos)


    #Getters
    def get_yardas(self):
        return self.__yardas

    def get_metros(self):
        return self.__metros

    def get_millas(self):
        return self.__millas

    def get_pulgadas(self):
        return self.__pulgadas

    #Metodos de instancia
    def __convertirMetrosPulgadas(self, metros):
        #El programa realizará la conversión de metros a pulgadas

        self.__pulgadas += metros * 39.37

    def __convertirMetrosYardas(self, metros):
        #El programa realizará la conversión de metros a yardas.
        self.__yardas += metros * 1.094

    def __convertirMetrosMillas(self, metros):
        #El programa realizará la conversión de metros a millas.
        self.__millas += metros * 1609


    #Metodo de clase
    @classmethod
    def convertirYardasCentimetros(cls, yardas):
        centimetros = yardas * 91.44;
        return centimetros

    #Sobrecarga de operadores

    def __str__(self):
        return "La sobrecarga es: " + str(self.convertirYardasCentimetros(10))

