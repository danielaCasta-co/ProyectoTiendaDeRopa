class User():
    def __init__(self, Userid, Password, RegisterDate, Name, Email):
        self.Userid = Userid
        self.Password = Password
        self.RegisterDate = RegisterDate
        self.Name = Name
        self.Email = Email
        
    def Login(self):
        pass
    
    def __init__(self):
        return self.Userid
    

class Customer(User):
    def __init__(self, Address, Customerld, AcountBalance):
        super().__init__(Customer)        
        self.Address = Address
        self.AcountBalance = AcountBalance
        self.Customerid = Customerld
        
    def Register(self):
        return self.Customer
    
    def Purchase(self):
        return self.Customer
    
class Administrador(User):
    def __init__():
        super().__init__(Administrador)
        
        
    def UpDateProducts(self):
        self.Administrador
        
Customer = Customer("laura, 1223325, laura123@gmail.com, 4, 5")
Administrador = Administrador("Juan, juan123@gmail.com")
        
        
