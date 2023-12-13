package template_method.java;

public abstract class CuentaBancaria {

	protected String cbu;
	protected double saldo;

	public CuentaBancaria(
		String unCbu, double unSaldoInicial
	) {
		this.cbu = unCbu;
		this.saldo = unSaldoInicial;
	}

	//Método Plantilla - Template Method
	protected final void plantillaExtraer(double unMonto) {
		this.hacerValidar(unMonto);
		this.extraerGancho(unMonto);
		this.informarGancho(unMonto);
	}

	// Método abstracto puro redefinible por las subclases
	protected abstract boolean hacerValidar(double unMonto);

	// Método gancho con implementación por defecto
	protected void extraerGancho(double unMonto) {
		this.saldo -= unMonto;
	}

	// Método gancho con implementación por defecto
	protected void informarGancho(double unMonto) {
		System.out.println("Se extrajo con éxito de la cuenta " + this.cbu + " $" + unMonto);
	}
	
}