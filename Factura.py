class Factura:
    NombreEmpresa: str
    Telefono: int
    Correo: bool
    NumeroRUT: int
    NumeroFactura: int
    ValorIVA: int

    def __init__(self):
        self.CarritoCompras = CarritoCompras()
        self.DetalleFactura = DetalleFactura ()
        self.Producto = Producto ()

        def Producto(self):
            Factura.Producto = Producto
        
        def NuevaCuenta(self):
            return "Nueva Cuenta"

        def Descuentos(self):
            return "Descuentos"

        def ValorTotal(self):
            return "Valor Total"