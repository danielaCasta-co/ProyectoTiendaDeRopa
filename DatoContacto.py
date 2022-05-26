from socketserver import DatagramRequestHandler
from Administrador import Contrasena


class DatoContacto:
        def __init__(self, Telefono, Direccion, Email, UsuarioPagina, ContrasenaPagina):
                self.Telefono = Telefono
                self.Direccion = Direccion
                self.Email = Email
                self.UsuarioPagina = UsuarioPagina
                self.ContrasenaPagina = ContrasenaPagina
                
        def getTelefono(self):
                return self.Telefono
        
        def getDireccion(self):
                return self.Direccion
        
        def getEmail(self):
                return self.Email
        
        def getUsuarioPagina(self):
                return self.UsuarioPagina
        
        def getContrasenaPagina(self):
                return self.ContrasenaPagina
        
        def ActualizarDatoContacto(self):
            print(self.getTelefono(), self.getDireccion(), self.getEmail(), self.getUsuarioPagina(), self.getContrasenaPagina())
        
        def ValidarEmail(self):
            print(self.getEmail())
        
Telefono = int(input("Ingrese el numero de telefono: "))
Direccion = input("Ingrese la direccion: ")  
Email = int(input("Ingrese el email: "))
UsuarioPagina = int(input("Ingrese el usuario de la pagina: "))
ContrasenaPagina = input("Ingrese la contrasena de la pagina: ")

DatoContacto = DatoContacto(Telefono, Direccion, Email, UsuarioPagina, ContrasenaPagina)
DatoContacto.ActualizarDatoContacto()
DatoContacto.ValidarEmail()
DatoContacto =DatoContacto
