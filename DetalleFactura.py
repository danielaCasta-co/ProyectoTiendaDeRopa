class DetalleFactura:
    def __init__(self, Producto, ValorUnitario, CantidadProducto):
        self.Producto = Producto
        self.ValorUnitario = ValorUnitario
        self.CantidadProducto = CantidadProducto
        
    def getProducto(self):
        return self.Producto
    
    def getValorUnitario(self):
        return self.ValorUnitario
    
    def getCantidadProducto(self):
        return self.CantidadProducto
    
    
    
    def Producto(self):
        return self.Producto
    
Producto = input("Digite el nombre del producto:")
ValorUnitario = int(input("Digite el valor unitario por producto:"))
CantidadProducto = int(input("Cantidad por producto:"))

DetalleFactura = DetalleFactura(Producto, ValorUnitario, CantidadProducto)
DetalleFactura.Producto()
DetalleFactura = DetalleFactura
