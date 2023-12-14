from abc import abstractmethod

class CuentaBancaria(object):

	cbu = "no_asignado"
	saldo = .0

	def __init__(self, unCbu, unSaldo):
		super()
		self.cbu = unCbu
		self.saldo = unSaldo
	
	def plantillaExtraer(self, unMonto):
		self.hacerValidar(unMonto)
		self.extraerGancho(unMonto)
		self.informarGancho(unMonto)

	@abstractmethod
	def hacerValidar(self, unMonto):
		return

	def extraerGancho(self, unMonto):
		self.saldo -= unMonto

	def informarGancho(self, unMonto):
		return f"Se extrajo con éxito de la cuenta {self.cbu} ${unMonto}"
	
	def __str__(self):
		return f"Cuenta bancaria -> cbu: {self.cbu} saldo: ${self.saldo}"