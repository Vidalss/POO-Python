import Convertidor
import AbsClass
from Convertidor import *
from AbsClass import *
from herencia.converter import *

def main():
    conv = convertidor(80, 20)
    print(conv.get_yardas())
    print(conv.get_metros())
    print(conv.get_millas())
    print(conv.get_pulgadas())

    print("Resultados de la clase abstracta ")
    print(AbsClass.yardasABS(20, 80))
    print(AbsClass.metrosABS(20,80))
    print(AbsClass.millasABS(20,80))
    print(AbsClass.pulgadasABS(20,80))

    print("Resultados de metodo de clase")
    print(conv.convertirYardasCentimetros(94))

    print("Sobrecarga de operadores")
    conv2 = convertidor(80,20)
    print(str(conv2.__str__()))


    print("Resultados de la herencia")
    converter = MetrosConvertidor(20,80)
    print(converter.getResult())
    converter1 = MillasConvertidor(20,80)
    print(converter1.getResult())
    converter2 = PulgadasConvertidor(20,80)
    print(converter2.getResult())
    converter3 = YardasConvertidor(20,80)
    print(converter3.getResult())
if __name__ == "__main__":
    main()