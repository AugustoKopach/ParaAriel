package entity;

public class Cliente {
	private Ciudad ciudadDondeVive;

	public Ciudad getCiudadDondeVive() {
		return ciudadDondeVive;
	}
	public void setCiudadDondeVive(Ciudad ciudadDondeVive) {
		this.ciudadDondeVive = ciudadDondeVive;
	}
	public Boolean puedeSerAtendidoPor(Vendedor vendedor) {
		return vendedor.puedeTrabajarEnCiudad(ciudadDondeVive);
	}
}
