class CajaDeAhorro extends CuentaBancaria {

	public constructor(
		unCbu: string, unSaldo: number = 0
	) {
		super(unCbu, unSaldo);
	}

	protected hacerValidar(unMonto: number) {
		return (
			(unMonto > 0) && (unMonto <= this.saldo)
		);
	}

}