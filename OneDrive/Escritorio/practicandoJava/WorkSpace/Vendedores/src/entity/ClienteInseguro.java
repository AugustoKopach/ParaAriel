package entity;

public class ClienteInseguro extends Cliente {


	public Boolean puedeSerAtendidoPor(Vendedor vendedor) {
		return super.puedeSerAtendidoPor(vendedor) && vendedor.esFirme() && vendedor.esVersatil();
	}
	
	
}
