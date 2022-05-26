class Usuario():
    def __init__(self,IdUsuario, FechaRegistro):
        self.IdUsuario = IdUsuario
        self.FechaRegistro = FechaRegistro

    def CrearUsuario(self):
        pass

    def EliminarUsuario(self):
        return "Eliminar Usuario"

    def __int__(self):
        return self.IdUsuario


class Cliente(Usuario):
    def __init__(self, Nombre, NumeroTarjeta, Edad, Sexo):
        super().__init__(Cliente)
        self.Nombre = Nombre
        self.NumeroTarjeta = NumeroTarjeta
        self.Edad = Edad
        self.Sexo = Sexo

    def EditarCliente(self):
        return self.Cliente

    def EliminarCliente(self):
        return "Eliminar Cliente"

class Administrador(Usuario):
    def __init__(self, Usuario, Contraseña):
        super().__init__("Administrador")
        self.Usuario = Usuario
        self.Contraseña  = Contraseña

    def CambiarContraseña(self):
        return self.Administrador
    
    def EliminarAdministrador(self):
        return self.Administrador

Cliente = Cliente("Laura", "1055568940", "21", "Femenino")
Administrador = Administrador("Juan", "123456")

print("Editar cliente:",Cliente.cliente())
print("Cambiar contraseña:", Administrador.administrador())
