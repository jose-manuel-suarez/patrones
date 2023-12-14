from CuentaBancaria import CuentaBancaria

class CajaDeAhorro(CuentaBancaria, object):

	def __init__(self, unCbu, unSaldo):
		super(unCbu, unSaldo)

	def hacerValidar(self, unMonto):
		return (unMonto > 0) and (unMonto <= self.__saldo)