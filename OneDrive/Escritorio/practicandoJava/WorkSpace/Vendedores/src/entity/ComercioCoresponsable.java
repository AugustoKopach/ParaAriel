package entity;

import java.util.Collection;

public class ComercioCoresponsable extends Vendedor{
	protected Collection <Ciudad> ciudadesConSucursales;


	public Boolean puedeTrabajarEnCiudad(Ciudad ciudad) {
	    return ciudadesConSucursales.stream().anyMatch(c -> c.equals(ciudad));
	}
}
