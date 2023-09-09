package entity;

import java.util.Collection;
import java.util.stream.Collectors;

public class Empresa {
	private Collection <CentroDeDist> centrosDeDistribucion;
	
	public Collection<Vendedor> VendedoresMasFlojos() {
	    return centrosDeDistribucion.stream()
	            .map(CentroDeDist::elVendedorMasFlojo)
	            .filter(vendedor -> vendedor != null)
	            .collect(Collectors.toList());
	}
}
