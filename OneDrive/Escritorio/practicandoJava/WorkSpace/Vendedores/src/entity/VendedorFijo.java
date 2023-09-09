package entity;

public class VendedorFijo extends Vendedor{
	private Ciudad ciudadDondeVive;
	
	public  Boolean puedeTrabajarEnCiudad(Ciudad ciudad) {
	  return 	ciudadDondeVive.equals(ciudad);
	}
}
