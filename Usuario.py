from ast import Pass
from binascii import a2b_base64
from re import A


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

    def CrearUsuario(self):
        return self.Cliente

    def EditarCliente(self):
        return "EditarCliente"

class Administrador(Usuario):
    def __init__(self, Usuario, Contraseña):
        super().__init__("Administrador")
        self.Usuario = Usuario
        self.Contraseña  = Contraseña

    def CrearUsuario(self):
        return self.Usuario

Cliente = Cliente("Laura")
Administrador = Administrador("Juan")
print(Administrador)
print(Administrador.EliminarUsuario())
print(Cliente.EliminarUsuario())
print(Administrador.CrearUsuario)
