package entity;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Optional;
import java.util.Set;

import Exception.VendedorExistenteException;
public class CentroDeDist {
    private Collection<Vendedor> vendedores = new ArrayList<Vendedor>();

    
    
    public CentroDeDist(Collection<Vendedor> vendedores) {
		super();
		this.vendedores = vendedores;
	}

	public Vendedor elVendedorMasFlojo() {
        Optional<Vendedor> minVendedor = vendedores.stream()
                .min(Comparator.comparingInt(Vendedor::PuntosXCert));
        return minVendedor.orElse(null); 
    }

	public Collection<Vendedor> getVendedores() {
		return vendedores;
	}

	public void setVendedores(Collection<Vendedor> vendedores) {
		this.vendedores = vendedores;
	}
	public Boolean puedeCubrir(Ciudad unaciudad) {
		return vendedores.stream().anyMatch(vend -> vend.puedeTrabajarEnCiudad(unaciudad));
	}
	
	public void contratarVendedor(Vendedor vendor) throws VendedorExistenteException {
	    if (vendedores.stream().anyMatch(ven -> ven.equals(vendor))) {
	        throw new VendedorExistenteException(vendor.getNombre() + " ya está adherido a la empresa");
	    } else {
	        this.vendedores.add(vendor);
	    }   
	}
	   public Set<Ciudad> ciudadesConRedundancia(Collection<Ciudad> ciudadesPreguntadas) {
	          Set<Ciudad> ciudadesRedundantes = new HashSet<>();
	          
	        for (Ciudad ciudad : ciudadesPreguntadas) {
	            int cantVendedores = 0;
	            for (Vendedor vendedor : vendedores) {
	                if (vendedor.puedeTrabajarEnCiudad(ciudad)) {
	                    cantVendedores++;
	                }
	            }
	            if (cantVendedores >= 2) {
	                ciudadesRedundantes.add(ciudad);
	            }
	        }
	        return ciudadesRedundantes;
	    }
	}
