
from CuentaBancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria, object):

	__descubierto = .0

	def __init__(self, unCbu, unSaldo, unLimiteDescubierto):
		super().__init__(unCbu, unSaldo)
		self.__descubierto = unLimiteDescubierto

	def hacerValidar(self, unMonto):
		return (unMonto > 0) and (unMonto <= self.saldo + self.__descubierto)
	
	def __str__(self):
		return super().__str__() + f" limite descubierto: ${self.__descubierto}"
	
"""
mi_cuenta = CuentaCorriente("35186490", 300.45, 1500)
print(mi_cuenta)
print(mi_cuenta.hacerValidar(1800.46))
"""