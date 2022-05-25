from mailbox import NoSuchMailboxError


class Cliente:
    def __init__(self, Nombre, NumeroTarjeta, Edad, Sexo, Pedido):
        self.Nombre = Nombre
        self.NumeroTarjeta = NumeroTarjeta
        self.Edad = Edad
        self.Sexo = Sexo
        self.Pedido = Pedido
        
    def getNombre(self):
        return self.Nombre
        
    def getNumeroTarjeta(self):
        return self.NumeroTarjeta
    
    def getEdad(self):
        return self.Edad
    
    def getSexo(self):
        return self.Sexo
    
    def getPedido(self):
        return self.Pedido
    
    def EditarCliente(self):
        print(self.getNombre(), self.getNumeroTarjeta(), self.getEdad(), self.getSexo(), self.getPedido())

    def EliminarCliente(self):
        print(self.getNombre(), self.getNumeroTarjeta(), self.getEdad(), self.getSexo(), self.getPedido())

Nombre = input("Ingrese el nombre: ")
NumeroTarjeta = int(input("Ingrese el numero de la tarjeta: "))
Edad = int(input("Ingrese la edad: "))
Sexo = input("Ingrese el sexo: ")
Pedido = input("Digitar el pedido: ")

Cliente = Cliente(Nombre, NumeroTarjeta, Edad, Sexo, Pedido)
Cliente.EditarCliente()
Cliente.EliminarCliente()
Cliente = Cliente
         
    