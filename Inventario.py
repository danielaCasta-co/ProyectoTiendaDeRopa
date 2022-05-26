class Inventario:
    def __init__(self, Referencia, Cantidad, Producto):
        self.Referencia = Referencia
        self.Cantidad = Cantidad
        self.Producto = Producto
    
    def getReferencia(self):
        return self.Referencia
    
    def getCantidad(self):
        return self.Cantidad
    
    def getProducto(self):
        return self.Producto
    
    def ActualizarInventario(self):
        print(self.getReferencia(), self.getCantidad(), self.getProducto())
    
    def ReiniciarInventario(self):
        print(self.getReferencia(), self.getCantidad(), self.getProducto())

Referencia = input("Referencia del producto:")
Cantidad = input("Cantidad por producto:")
Producto = int(input("Producto:"))

Inventario = Inventario(Referencia, Cantidad, Producto)
Inventario.ActualizarInventario()
Inventario.ReiniciarInventario()
Inventario = Inventario  
