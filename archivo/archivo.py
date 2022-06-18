from abc import ABCMeta

class Archivos(ABCMeta):

    # Método estático
    @staticmethod
    def convertirUnidades(pies, metros):
        yardas = round((metros * 1.094) + (pies / 3.281))
        millas = round((metros * 1609) + (pies / 3.281))
        pulgadas = round((metros * 39.37) + (pies / 3.281))
        metros = round(metros + (pies / 3.281))

        unidades = [metros, yardas, millas, pulgadas]
        return unidades


class pruebaArchivos:

    def leerArchivo(self, archivo):
        file = open(archivo, 'r')
        lineas = []
        lineas_archivo = []
        for linea in file.readlines():
            lineas.append(linea.replace('\n', '').split("#"))
        file.close()
        for f in range(0, len(lineas)):
            try:
                lineas_archivo.append([int(lineas[f][0]), int(lineas[f][1])])
            except ValueError:
                lineas_archivo.append([0, 0])
        return lineas_archivo

    def calcularResultados(self, lista):
        resultados = []
        for f in range(0, len(lista)):
            resultados.append(Archivos.convertirUnidades(
                lista[f][0],lista[f][1]))
        return resultados

    def guardarResultados(self, entrada, resultados):
        file = open("resultados.txt", 'w')
        file.write('Metros#Yardas#Millas#Pulgadas\n')
        for f in range(0, len(entrada)):
            linea = str(entrada[f][0]) + '#' + \
                    str(entrada[f][1]) + '#' + \
                    '#' + str(resultados[f]) +'\n'
            file.write(linea)
        file.close()

if __name__ == "__main__":
    prueba = pruebaArchivos()
    archivo = []
    archivo = prueba.leerArchivo("si.txt")
    print(archivo)
    resultado = prueba.calcularResultados(archivo)
    prueba.guardarResultados(archivo, resultado)