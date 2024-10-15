import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros, FaltanParametros


class PruebaOperacionesEnteros(unittest.TestCase):

    def setUp(self):
        """Configura valores comunes para las pruebas."""
        self.numeros_comunes = [18, 24, 30]
        self.numeros_adicionales = [4]

    def test_MCD_dos_numeros_positivos_retorna_MCD(self):
        """Prueba que el MCD de dos números positivos se calcule correctamente."""
        operacion = OperacionesEnteros(self.numeros_comunes[:2])
        resultado_actual = operacion.calcularMCD()
        self.assertEqual(resultado_actual, 6)

    def test_MCD_tres_numeros_positivos_retorna_MCD(self):
        """Prueba que el MCD de tres números positivos se calcule correctamente."""
        operacion = OperacionesEnteros(self.numeros_comunes)
        resultado_actual = operacion.calcularMCD()
        self.assertEqual(resultado_actual, 6)

    def test_MCD_cuatro_numeros_positivos_retorna_MCD(self):
        """Prueba que el MCD de cuatro números positivos se calcule correctamente."""
        operacion = OperacionesEnteros(self.numeros_comunes + self.numeros_adicionales)
        resultado_actual = operacion.calcularMCD()
        self.assertEqual(resultado_actual, 2)

    def test_MCD_un_numero_positivo_lanza_excepcion(self):
        """Prueba que se lance una excepción al calcular el MCD con un solo número."""
        operacion = OperacionesEnteros([18])
        with self.assertRaises(FaltanParametros):
            operacion.calcularMCD()

    def test_MCD_una_cadena_lanza_excepcion(self):
        """Prueba que se lance una excepción al pasar una cadena como argumento."""
        operacion = OperacionesEnteros(["18a", 13])
        with self.assertRaises(ValueError):
            operacion.calcularMCD()


if __name__ == '__main__':
    unittest.main()
