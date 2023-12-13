class CuentaCorriente extends CuentaBancaria {

	descubierto: number;

	constructor(
		unCbu: string, unSaldo: number, unDescubierto: number
	) {
		super(unCbu, unSaldo);
		this.descubierto = unDescubierto;
	}

	protected hacerValidar(unMonto: number) {
		return (
			(unMonto > 0) && (unMonto <= this.saldo + this.descubierto)
		);
	}

}