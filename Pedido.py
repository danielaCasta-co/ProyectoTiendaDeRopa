class Pedido:
    def __init__(self, Cantidad, Producto, PedidoCliente):
        self.Cantidad = Cantidad
        self.Producto = Producto
        self.PedidoCliente = PedidoCliente
        
    def getCantidad(self):
        return self.Cantidad
    
    def getProducto(self):
        return self.Producto
    
    def getPedidoCliente(self):
        return self.PedidoCliente
    
    def ModificarPedido(self):
        print(self.getCantidad(), self.getProducto(), self.getPedidoCliente())

    def ReiniciarFactura(self):
        print(self.getCantidad(), self.getProducto(), self.getPedidoCliente())

Cantidad = int(input("Digite la cantidad del producto:"))
Producto = input("Dgite el producto:")
PedidoCliente = input("Digite el pedido del cliente:")

Pedido = Pedido(Cantidad, Producto, PedidoCliente)
Pedido.ModificarPedido()
Pedido.ReiniciarFactura()
Pedido = Pedido