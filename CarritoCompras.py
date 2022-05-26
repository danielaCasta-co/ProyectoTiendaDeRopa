class CarritoCompras:
    def __init__(self, Codigo, Usuario,Pedido,Factura,MetodoPago):
        self.Codigo = Codigo
        self.Usuario = Usuario
        self.Pedido = Pedido
        self.Factura = Factura
        self.MetodoPago = MetodoPago
    
    def getCodigo(self):
        return self.Codigo    
    def getUsuario(self):
        return self.Usuario
    def getPedido(self):
        return self.Pedido
    def getFactura(self):
        return self.Factura
    def getMetodoPago(self):
        return self.MetodoPago
    
    def ReiniciarCarritoCompras(self):
        print(self.getUsuario(), self.getPedido(), self.getFactura(), self.getMetodoPago())
            
Codigo = int(input("Ingrese el codigo: "))
Usuario = input("Ingrese el nombre de usuario: ")
Pedido = int(input("Ingrese el pedido: "))
Factura = int(input("Ingrese el numero de factura: "))
MetodoPago = input("Ingrese el metodo de pago: ")

CarritoCompras = CarritoCompras(Codigo, Usuario, Pedido, Factura, MetodoPago)
CarritoCompras.ReiniciarCarritoCompras()
CarritoCompras = CarritoCompras
