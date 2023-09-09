package entity;

import java.util.Collection;

public class Provincia {
	private String nombre;
	private Collection <Ciudad> ciudadesDeProvincia; 
	
	public Boolean pertenece(Ciudad unaCiudad) {
		return ciudadesDeProvincia.contains(unaCiudad);
	}
	public String nombreDeLaProvincia(){
		return nombre;
	}
}

