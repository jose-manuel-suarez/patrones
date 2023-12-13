package template_method.java;

public class CajaDeAhorro extends CuentaBancaria {

	public CajaDeAhorro(
		String unCbu, double unSaldoInicial
	) {
		super(unCbu, unSaldoInicial);
	}

	@Override
	protected boolean hacerValidar(double unMonto) {
		return (
			(unMonto > 0) && (unMonto <= this.saldo)
		);
	}

}