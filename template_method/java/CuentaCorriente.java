package template_method.java;

public class CuentaCorriente extends CuentaBancaria {
	
	private double descubierto; //Es el saldo que la cuenta permite en rojo

	public CuentaCorriente(
		String unCbu, double unSaldoInicial, double unLimiteDescubierto
	) {
		super(unCbu, unSaldoInicial);
		this.descubierto = unLimiteDescubierto;
	}

	@Override
	protected boolean hacerValidar(double unMonto) {
		return (
			(unMonto > 0) && (unMonto <= this.saldo + this.descubierto)
		);
	}

}
