package entity;

public class ClienteHumanista extends Cliente {

	public Boolean puedeSerAtendidoPor(Vendedor vendedor) {
		
		return super.puedeSerAtendidoPor(vendedor) && (vendedor  instanceof ComercioCoresponsable);
	}
	
}
