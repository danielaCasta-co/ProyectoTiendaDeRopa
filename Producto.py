class Producto:
    def __init__(self, ReferenciaProducto, NombreProducto, Categoria, Genero, Talla, Color, Marca):
        self.ReferenciaProducto = ReferenciaProducto
        self.NombreProducto = NombreProducto
        self.Categoria = Categoria
        self.Genero = Genero
        self.Talla = Talla
        self.Color = Color
        self.Marca = Marca
        
    def getReferenciaProducto(self):
        return self.ReferenciaProducto
    
    def getNombreProducto(self):
        return self.NombreProducto
    
    def getCategoria(self):
        return self.Categoria
    
    def getGenero(self):
        return self.Genero
    
    def getTalla(self):
        return self.Talla
    
    def getColor(self):
        return self.Color
    
    def getMarca(self):
        return self.Marca

    def ModificarProducto(self):
        print(self.getReferenciaProducto(), self.getNombreProducto(), self.getCategoria(), self.getGenero(), self.getTalla(), self.getColor(), self.getMarca())

ReferenciaProducto = int(input("Referencia del producto:"))          
NombreProducto = input("Digite el nombre del producto:")
Categoria = input("Digite la categoria:")
Genero = input("Digite el genero:")
Talla = input("Digite la talla:")
Color = input("Digite color:")
Marca = input("Digite la marca:")

Producto = Producto(ReferenciaProducto, NombreProducto, Categoria, Genero, Talla, Color, Marca)
Producto.ModificarProducto()
Producto = Producto
