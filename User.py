class User():
    def __init__(self, Userid, Password, RegisterDate):
        self.Userid = Userid
        self.Password = Password
        self.RegisterDate = RegisterDate
        
    def Login(self):
        pass
    
    def __init__(self):
        return self.Userid
    

class Customer(User):
    def __init__(self, Name, Address, Email, Customerld, AcountBalance):
        super().__init__(Customer)
        self.Name = Name
        self.Address = Address
        self.Email = Email
        self.Customer = Customer
        self.AcountBalance = AcountBalance
        
    def Register(self):
        return self.Customer
    
    def Purchase(self):
        return self.Customer
    
class Administrador(User):
    def __init__(self, Name, Email):
        super().__init__("Administrador")
        self.Name = Name
        self.Email = Email
        
    def UpDateProducts(self):
        self.Administrador
        
Customer = Customer("laura, 1223325, laura123@gmail.com, 4, 5")
Administrador = Administrador("Juan, juan123@gmail.com")
        
