class MetodoPago:
        def __init__(self, IdPago, TipoPago):
                self.IdPago = IdPago
                self.TipoPago = TipoPago
        
        def getIdPago(self):
                return self.IdPago
        
        def getTipoPago(self):
                return self.TipoPago
        
        def CrearMetodoPago(self):
            print(self.getIdPago(), self.getTipoPago())
        
        def EliminarMetodoPago(self):
            print(self.getIdPago(), self.getTipoPago())    
        
IdPago = int(input("Digite el ID de pago:"))
TipoPago =input("Dgite el tipo de pago:") 

MetodoPago = MetodoPago(IdPago, TipoPago)
MetodoPago.CrearMetodoPago()
MetodoPago.EliminarMetodoPago()
MetodoPago = MetodoPago