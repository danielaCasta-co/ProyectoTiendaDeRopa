class Administrador:
        def __init__(self,Usuario,Contrasena):
                self.Usuario = Usuario
                self.Contrasena = Contrasena
                
        def getUsuario(self):
                return self.Usuario
        
        def getContrasena(self):
                return self.Contrasena
        
        def CrearContrasena(self):
                print(self.getUsuario(), self.getContrasena())

Usuario = input("Ingrese el usuario: ")
Contrasena = input("Ingrese la contraseña: ")
Administrador = Administrador(Usuario,Contrasena)
Administrador.CrearContrasena()
administrador = Administrador()
