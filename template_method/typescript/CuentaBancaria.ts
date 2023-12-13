abstract class CuentaBancaria {

	protected cbu: string;
	protected saldo: number;

	public constructor(
		unCbu: string, unSaldo: number = 0
	) {
		this.cbu = unCbu;
		this.saldo = unSaldo;
	}

	//Método Plantilla - Template Method
	protected plantillaExtraer(unMonto: number): void {
		this.hacerValidar(unMonto);
		this.extraerGancho(unMonto);
		this.informarGancho(unMonto);
	}

	protected abstract hacerValidar(unMonto: number);

	// Método gancho con implementación por defecto
	protected extraerGancho(unMonto: number): void {
		this.saldo -= unMonto;
	}

	// Método gancho con implementación por defecto
	protected informarGancho(unMonto: number): void {
		console.log("Se extrajo con éxito de la cuenta " + this.cbu + " $" + unMonto);
	}

}