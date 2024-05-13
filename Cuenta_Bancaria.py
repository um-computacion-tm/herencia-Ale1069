class CuentaBancaria:
    def __init__(self, titular, monto, numero):
        self.__titular__ = titular
        self.__saldo__ = monto
        self.__numero__ = numero

    def dame_saldo(self):
        return self.__saldo__

    def deposito(self, monto_deposito):
        self.__saldo__ += monto_deposito

    def retirar(self, monto_retiro):
        self.__saldo__ -= monto_retiro

class CajaAhorro(CuentaBancaria):
    def retirar(self, monto_retiro):
        if self.__saldo__ - monto_retiro < 0:
            print("no te alcanza, prueba otro monto")
        else:
            super().retirar(monto_retiro)

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, monto, numero, limite_descubierto):
        super().__init__(titular, monto, numero)
        self.__limite_descubierto__ = limite_descubierto

    def retirar(self, monto_retiro):
        if self.__saldo__ - monto_retiro < -self.__limite_descubierto__:
            self.__saldo__ = -self.__limite_descubierto__
        else:
            super().retirar(monto_retiro)


cuenta_ahorro_gabi = CajaAhorro('Gabriel', 10000, '431432143')
print('inicio Caja ahorro Gabi', cuenta_ahorro_gabi.dame_saldo())
cuenta_ahorro_gabi.deposito(100)
cuenta_ahorro_gabi.deposito(200)
print('Luego deposito CA Gabi', cuenta_ahorro_gabi.dame_saldo())
cuenta_ahorro_gabi.retirar(10000)
print('Luego retiro CA Gabi', cuenta_ahorro_gabi.dame_saldo())
cuenta_ahorro_gabi.retirar(10000)
print('Luego segundo retiro CA Gabi', cuenta_ahorro_gabi.dame_saldo())

print('==================')

cuenta_corriente_elio = CuentaCorriente('Elio', 3000, '474563456', 5000)

print('inicio Cuenta corriente Elio', cuenta_corriente_elio.dame_saldo())
cuenta_corriente_elio.deposito(2000)
cuenta_corriente_elio.deposito(800)
print('Luego CC  Elio', cuenta_corriente_elio.dame_saldo())
cuenta_corriente_elio.retirar(5000)
print('Luego primer retiro CC Elio', cuenta_corriente_elio.dame_saldo())
cuenta_corriente_elio.retirar(5000)
print('Luego segundo retiro CC Elio', cuenta_corriente_elio.dame_saldo())

cuenta_corriente_elio.retirar(5000)
print('Luego tercer retiro retiro CC Elio', cuenta_corriente_elio.dame_saldo())