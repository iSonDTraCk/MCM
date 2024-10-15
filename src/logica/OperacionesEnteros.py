from src.logica.FaltanParametros import FaltanParametros


class OperacionesEnteros:
    def __init__(self, numeros):
        self.__numeros = numeros

    def calcularMCD(self):
        if len(self.__numeros) < 2:
            raise FaltanParametros
        elif len(self.__numeros) > 1:
            return self.MCDMasDosNumeros()
        else:
            return 0

    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1

    def MCDMasDosNumeros(self):
        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError

        cantidadNumeros = len(self.__numeros)
        mcd = self.MCD(self.__numeros[0], self.__numeros[1])
        i = 0
        while i < (cantidadNumeros - 2):
            mcd = self.MCD(mcd, self.__numeros[i + 2])
            i += 1
        return mcd

    def calcularMCM(self):
        if len(self.__numeros) < 2:
            raise ValueError

        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError


        mcd = self.calcularMCD()

        # MCM(a, b, c) = (a * b * c) / MCD(a, b, c)
        a, b, c = self.__numeros
        mcm = (a * b * c) // mcd

        return mcm


# Ejemplo de uso:
if __name__ == "__main__":
    numeros = [12, 15, 20]
    operaciones = OperacionesEnteros(numeros)
    print("El MCD de", numeros, "es:", operaciones.calcularMCD())
    print("El MCM de", numeros, "es:", operaciones.calcularMCM())
