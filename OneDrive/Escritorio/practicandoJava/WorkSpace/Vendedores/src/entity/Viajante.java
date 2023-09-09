package entity;

import java.util.Collection;

public class Viajante extends Vendedor {
	protected Collection <Provincia> provinciaHabilitado;
	
	public Boolean puedeTrabajarEnCiudad(Ciudad ciudad) {
		return provinciaHabilitado.stream().anyMatch(prov -> prov.pertenece(ciudad));
	}
	
	
}
