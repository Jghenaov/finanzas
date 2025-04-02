from abc import ABC, abstractmethod

class MetodoPago(ABC):

    @abstractmethod
    def procesar_pago(self, monto):
        pass

class PagoTarjea(MetodoPago):
    def __init__(self, monto):
        self.monto = monto

    def procesar_pago(self, monto):
        print(f'Pago de {monto:.2f} realizado con tarjeta de credito/debito.')

class PagoEfectivo(MetodoPago):
    def __init__(self, monto):
        self.monto = monto

    def procesar_pago(self, monto):
        print(f'Pago de {monto:.2f} realizado con exito.')

class PagoPaypal(MetodoPago):
    def __init__(self, monto):
        self.monto = monto

    def procesar_pago(self, monto):
        print(f'Pago de {monto:.2f} realizado exitosamente con PayPal.')

class FabricaPagos:

    @staticmethod
    def generador_pagos(tipo, monto):
        if tipo == 'tarjeta':
            return PagoTarjea(monto)
        elif tipo == 'efectivo':
            return PagoEfectivo(monto)
        elif tipo == 'paypal':
            return PagoPaypal(monto)
        else:
            print(f'El metodo de pago {tipo} no esta disponible para el pago. ')
            return None

        
        
pagos = input('Ingrese su metodo de pago; tarjeta/efectivo/paypal: ')

try:

    cantidad = float(input('Cual es el monto a pagar: '))
    metodo_pago = FabricaPagos.generador_pagos(pagos, cantidad)
    if metodo_pago:
            metodo_pago.procesar_pago(cantidad)
except ValueError:
    print('Error: Ingrese un monto valido.')









    
