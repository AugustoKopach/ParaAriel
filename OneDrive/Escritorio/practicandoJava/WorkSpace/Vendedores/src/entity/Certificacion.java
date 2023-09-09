package entity;

public class Certificacion {
	protected Integer puntuacionQueOtorga;
	protected Boolean esSobreProductos;
	// Attributes

	public Integer getPuntuacionQueOtorga() {
		return puntuacionQueOtorga;
	}

	public void setPuntuacionQueOtorga(Integer puntuacionQueOtorga) {
		this.puntuacionQueOtorga = puntuacionQueOtorga;
	}
	
	public Boolean getEsSobreProductos() {
		return esSobreProductos;
	}
	
	public void setEsSobreProductos(Boolean esSobreProductos) {
		this.esSobreProductos = esSobreProductos;
	}
	public Boolean noEsSobreProd() {
		return !esSobreProductos;
	}

}
