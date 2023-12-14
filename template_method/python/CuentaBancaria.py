from abc import abstractmethod

class CuentaBancaria:

	__cbu = "no_asignado"
	__saldo = .0

	def __init__(self, unCbu, unSaldo):
		self.__cbu = unCbu
		self.__saldo = unSaldo
	
	def plantillaExtraer(self, unMonto):
		self.hacerValidar(unMonto)
		self.extraerGancho(unMonto)
		self.informarGancho(unMonto)

	@abstractmethod
	def hacerValidar(self, unMonto):
		return

	def extraerGancho(self, unMonto):
		return

	def informarGancho(self, unMonto):
		return
	
	def __str__(self):
		return f"Cuenta bancaria -> {self.__cbu} saldo ${self.__saldo}"
	
mi_cuenta = CuentaBancaria("35186486", 300.44)
print(mi_cuenta)
