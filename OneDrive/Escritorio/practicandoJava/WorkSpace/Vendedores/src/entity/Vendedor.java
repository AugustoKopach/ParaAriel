package entity;
import java.util.ArrayList;
import java.util.Collection;

import Exception.VendedorExistenteException;
public abstract class Vendedor  {
	private String nombre;
	private Integer idVendedor;
	private Collection<Cliente> clientesAsignados = new ArrayList<>();
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public Collection<Certificacion> getCertificaciones() {
		return certificaciones;
	}

	public void setCertificaciones(Collection<Certificacion> certificaciones) {
		this.certificaciones = certificaciones;
		
	}


	@Override
	public boolean equals(Object obj) {
	
		return  this.idVendedor.equals(((Vendedor)obj).getIdVendedor());
	}


	/**
	 * @return the idVendedor
	 */
	public Integer getIdVendedor() {
		return idVendedor;
	}

	/**
	 * @param idVendedor the idVendedor to set
	 */
	public void setIdVendedor(Integer idVendedor) {
		this.idVendedor = idVendedor;
	}


	protected Collection<Certificacion> certificaciones;
	
	public Boolean esVersatil() {
		return certificaciones.stream().anyMatch(Certificacion :: getEsSobreProductos) && (certificaciones.stream().anyMatch(Certificacion :: noEsSobreProd))
				&& (certificaciones.size() >= 3 );
		}
	public Boolean esFirme() {
		return (this.PuntosXCert() >= 30);
		}
	public Integer PuntosXCert() {
		return (certificaciones.stream().mapToInt(Certificacion ::  getPuntuacionQueOtorga)
				 .sum());
	}
	
	public abstract Boolean puedeTrabajarEnCiudad(Ciudad ciudad);
	
	public void asignarCliente(Cliente srcliente) throws VendedorExistenteException {
	    if (srcliente.puedeSerAtendidoPor(this)) {
	        clientesAsignados.add(srcliente);
	    } else {
	        throw new VendedorExistenteException("El vendedor no puede atender a este cliente.");
	    }
	}

}