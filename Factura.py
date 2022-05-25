class Factura:
    def __init__(self, NombreEmpresa, Producto, DetalleFactura, Telefono, Correo, CarritoCompras, NumeroRUT, NumeroFactura, ValorIVA):
        self.NombreEmpresa = NombreEmpresa
        self.Producto = Producto
        self.DetalleFactura = DetalleFactura
        self.Telefono = Telefono
        self.Correo = Correo
        self.CarritoCompras = CarritoCompras
        self.NumeroRUT = NumeroRUT
        self.NumeroFactura = NumeroFactura
        self.ValorIVA = ValorIVA
        
    def getNombreEmpresa(self):
        return self.NombreEmpresa
    
    def getProdcuto(self):
        return self.Producto
    
    def getDetalleFactura(self):
        return self.DetalleFactura
    
    def getTelefono(self):
        return self.Telefono
    
    def getCorreo(self):
        return self.Correo
    
    def getCarritoCompras(self):
        return self.CarritoCompras
    
    def getNumeroRUT(self):
        return self.NumeroRUT
    
    def getNumeroFactura(self):
        return self.NumeroFactura
    
    def getValorIVA(self):
        return self.ValorIVA
    
    
    def Producto(self):
        return self.Producto
    
    def NuevaVenta(self):
        print(self.getNombreEmpresa(), self.getProdcuto(), self.getDetalleFactura(), self.getTelefono(), self.getCorreo(), self.getCarritoCompras(), self.getNumeroRUT(), self.getNumeroFactura(), self.getValorIVA())

    def Descuentos(self):
        print(self.getNombreEmpresa(), self.getProdcuto(), self.getDetalleFactura(), self.getTelefono(), self.getCorreo(), self.getCarritoCompras(), self.getNumeroRUT(), self.getNumeroFactura(), self.getValorIVA())
            
    def ValorTotal(self):
        print(self.getNumeroFactura(), self.getCarritoCompras())
        
        
NombreEmpresa = input("Nombre de la empresa:")
Producto = input("Digite el primer producto:")
DetalleFactura = input("Detalle de la factura:")
Telefono = int(input("Digite el telefono:"))
Correo = input("Digite el correo electronico:")
CarritoCompras = input("Carrito de compras:")
NumeroRUT = input("Numero del RUT:")
NumeroFactura = input("Numero de la factura:")
ValorIVA = int(input("Valor con IVA:"))

Factura = Factura(NombreEmpresa, Producto, DetalleFactura, Telefono, Correo, CarritoCompras, NumeroRUT, NumeroFactura, ValorIVA)
Factura.NuevaVenta()
Factura.Descuentos()
Factura.ValorTotal()
Factura = Factura