
from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass        
    
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        self.pi = 3.1416

    def area(self):
        bs = self.pi * (self.radio ** 2)
        print(f'El area del circulo es {bs}.')

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    #para el trinagulo
    def area(self):
        res = (self.base * self.altura) / 2
        print(f'El area del triangulo es {res}.')
    

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    #Para el cuadrado
    def area(self):
        rs = self.lado ** 2
        print(f'El area del cuadrado es {rs}.')


def crear_figura(tipo, *args):
   
        if tipo == 'circulo':
            return Circulo(*args)
        elif tipo == 'triangulo':
            return Triangulo(*args)
        elif tipo == 'cuadrado':
            return Cuadrado(*args)
        else:
            print(f'La figura{tipo} no es valida.')

circulo = crear_figura('circulo', 33)
triangulo = crear_figura('triangulo',32,25)
cuadrado = crear_figura('cuadrado',56)

cuadrado.area()
triangulo.area()
circulo.area()







    
        



        
        