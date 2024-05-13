import unittest


class CajaAhorro:

    def __init__(self, titular, monto, numero):
        self.__titular__ = titular
        self.__saldo__ = monto
        self.__numero__ = numero

    def dame_saldo(self):
        return self.__saldo__
    
    class TestCajaAhorro(unittest.TestCase):
        def setUp(self):
            self.cuenta = CajaAhorro('Gabriel', 10000, '431432143')

    def test_deposito(self):
        self.cuenta.deposito(100)
        self.assertEqual(self.cuenta.dame_saldo(), 10100)

    def test_retiro_suficiente(self):
        self.cuenta.retirar(5000)
        self.assertEqual(self.cuenta.dame_saldo(), 5000)

    def test_retiro_insuficiente(self):
        self.cuenta.retirar(15000)
        self.assertEqual(self.cuenta.dame_saldo(), 10000)

class CuentaCorriente:
    def __init__(self, titular, monto, numero, limite_descubierto):
        self.__titular__ = titular
        self.__saldo__ = monto
        self.__numero__ = numero
        self.__limite_descubierto__ = limite_descubierto

    def dame_saldo(self):
        return self.__saldo__
    
class TestCuentaCorriente(unittest.TestCase):
    def setUp(self):
        self.cuenta = CuentaCorriente('Elio', 3000, '474563456', 5000)

    def test_deposito(self):
        self.cuenta.deposito(2000)
        self.assertEqual(self.cuenta.dame_saldo(), 5000)

    def test_retiro_en_descubierto(self):
        # Intenta retirar más de lo que hay y dentro del límite de descubierto
        self.cuenta.retirar(6000)
        self.assertEqual(self.cuenta.dame_saldo(), -3000)

    def test_retiro_fuera_descubierto(self):
        # Intenta retirar más de lo que hay y fuera del límite de descubierto
        self.cuenta.retirar(10000)
        self.assertEqual(self.cuenta.dame_saldo(), -5000)


cuenta_ahorro_gabi = CajaAhorro('Gabriel', 10000, '431432143')
cuenta_ahorro_elio = CajaAhorro('Elio', 400000, '474563456')
print(cuenta_ahorro_gabi.dame_saldo())
print(cuenta_ahorro_elio.dame_saldo())


cuenta_corriente_gabi = CuentaCorriente('Gabriel', 2000, '431432143', 1000000)
cuenta_corriente_elio = CuentaCorriente('Elio', 3000, '474563456', 2000000)
print(cuenta_corriente_gabi.dame_saldo())
print(cuenta_corriente_elio.dame_saldo())

if __name__ == '__main__':
    unittest.main()