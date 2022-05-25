class Devoluciones:
    def __init__(self, IdDevoluciones, Factura, Fecha):
        self.IdDevoluciones = IdDevoluciones
        self.Factura = Factura
        self.Fecha = Fecha

    def getIdDevoluciones(self):
        return self.IdDevoluciones
    
    def getFactura(self):
        return self.Factura
    
    def getFecha(self):
        return self.Fecha
    
    def Ingresar(self):
        print(self.IdDevoluciones())
    
    def Modificar(self):
        print(self.IdDevoluciones(), self.Fecha(), self.Factura())
            
    def Eliminar(self):
        print(self.IdDevoluciones())
        
    def Consultar(self):
        print(self.IdDevoluciones())
     
     
        
    def Producto(self):
        return self.Producto
    
    def CarritoCompras(self):
        return self.CarritoCompras

IdDevoluciones = int(input("Digite el ID:"))
print(IdDevoluciones)
Factura = str(input("Digite el numero de la factura:"))
print(Factura)
Fecha = int(input("Dgite la fecha de compra:"))
print(Fecha) 
 
Devoluciones = Devoluciones(IdDevoluciones, Factura, Fecha)  
print(Devoluciones.Ingresar())
print(Devoluciones.Modificar())
print(Devoluciones.Eliminar())
print(Devoluciones.Consultar())
Devoluciones = Devoluciones