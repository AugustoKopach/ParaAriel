package entity;

public class ClienteDetallista extends Cliente {


	public Boolean puedeSerAtendidoPor(Vendedor vendedor) {
		return super.puedeSerAtendidoPor(vendedor) &&
				vendedor.getCertificaciones().stream().filter(cer -> cer.getEsSobreProductos()).count() > 3;
	}
}
