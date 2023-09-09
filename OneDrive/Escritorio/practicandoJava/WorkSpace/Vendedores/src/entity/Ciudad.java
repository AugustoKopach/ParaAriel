package entity;

public class Ciudad {
	private String nombreCiudad;
	private Integer codigoPostal;
	

	public boolean equals(Object obj) {
		    if (this == obj) {
		        return true; 
		    }
		    if (obj == null || getClass() != obj.getClass()) {
		        return false; 
		    }
		    Ciudad otraCiudad = (Ciudad) obj;
		    return codigoPostal != null && codigoPostal.equals(otraCiudad.codigoPostal);
		}
	
	public String getNombreCiudad() {
		return nombreCiudad;
	}
	public void setNombreCiudad(String nombreCiudad) {
		this.nombreCiudad = nombreCiudad;
	}
	
}
