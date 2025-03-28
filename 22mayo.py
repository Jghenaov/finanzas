"""¡Buena elección! Aquí tienes las pistas para tu Calculadora de Gastos:
📌 Requisitos del programa:

    Registrar ingresos y gastos

        Preguntar al usuario si quiere agregar un ingreso o un gasto.

        Guardar la cantidad y una descripción opcional (ejemplo: "Sueldo", "Comida", "Transporte").

    Calcular saldo disponible

        Sumar todos los ingresos.

        Restar todos los gastos.

        Mostrar el saldo actual.

    Mostrar un resumen

        Lista de ingresos y gastos con sus montos.

        Total de ingresos y total de gastos.

    Menú de opciones

        Agregar ingreso.

        Agregar gasto.

        Ver saldo.

        Ver historial.

        Salir.

🔥 Extras (si quieres agregar más dificultad):

    Guardar los datos en un archivo .txt o .json.

    Mostrar un análisis de gastos por categoría.

    Generar reportes simples."""

from abc import ABC, abstractmethod
from os import system




class Registro(ABC):
    
    ingresos = 0
    saldo_total = 0
    historial = []

    def __init__(self, cantidad, tipo_registro):
        self.tipo = tipo_registro
        self.cantidad = cantidad
        

        
    @abstractmethod
    def actualizar(self):
        pass


class Ingresos(Registro):
    
    def __init__(self, cantidad, tipo_registro):
        super().__init__(cantidad, tipo_registro)
        self.ingresos = []

    def __str__(self):
        return f'Ingresos totales: {Registro.ingresos}'
    
    
    
    def regitrar_ingreso(self):
        
        if self.tipo not in ['sueldo fijo', 'dividendos', 'independientes', 'otros']:
            raise ValueError(f'El tipo de ingreso {self.tipo} no es valido')
        if self.cantidad     <= 0:
            raise ValueError('La cantidad debe ser mayor a 0')  
        Registro.ingresos += self.cantidad 
        Registro.saldo_total += self.cantidad
        nuevo_ingreso = {'Cantidad': self.cantidad, 'Tipo de registro': self.tipo}        
        self.ingresos.append(nuevo_ingreso)
        Registro.historial.append(nuevo_ingreso)     
    
    def actualizar(self):
        
        for ing in self.ingresos:
            print(ing)
            
            
def historial_ingresos():
    for i, ingreso in enumerate(Registro.historial, 1):
        print(f'{i}. {ingreso}')       
        
class Gastos(Registro):

    def __init__(self, cantidad, tipo_registro):
        super().__init__(cantidad, tipo_registro)
        self.egresos = []

    def __str__(self):
        return f'Cantidad egresos: {self.cantidad}, Tipo: {self.tipo}'
    
    def regitrar_ingreso(self):
        
        while True:
            egreso = int(input('Cuanto dinero gasto:  '))
            tipoEgreso = input('Cual es el tipo de egreso:(Transporte, alimentacion, servicios, ocio, hogar, cuidado personal,Otros) ').lower()
            if tipoEgreso not in ['Transporte', 'alimentacion', 'servicios', 'ocio', 'hogar', 'cuidado personal','Otros']:
                return(f'El tipo de egreso {tipoEgreso} no es valido')
            if egreso <= 0:
                raise ValueError('La cantidad debe ser mayor a 0')            
            self.cantidad += egreso
            

    def actualizar(self):
        nuevo_egreso = {'Cantidad': self.cantidad, 'Tipo de registro': self.tipo}        
        self.egresos.append(nuevo_egreso)
        self.historial.append(nuevo_egreso)





def menu():
    while True:
        print('MENU PRINCUPAL.')
        print('********************************')
        print('1. Ingresos')   
        print('2. Egresos')
        print('3. Salir')
        print('********************************')
        
        opcion = int(input('Elige una opcion: '))
        system('clear')
        if opcion == 1:
            try:    
                ingreso = int(input('Cuanto es el ingreso:  '))
                tipoIngreso = input('Cual es el tipo de ingreso:(Sueldo fijo, Dividendos, Independientes, Otros) ').lower()
                ing = Ingresos(ingreso, tipoIngreso)
                ing.regitrar_ingreso()
                historial_ingresos()                
                ing.actualizar()
                print(Ingresos)
            except ValueError as e:
                print(f'ERROR: {e}')
 
        

menu()











"""ingresos = []
gastos = []
sueldo = 0

def registrar_ingresos(cantidad, tipo_ingreso,fecha):
    global sueldo
    nuevo_ingreso = {'Cantidad': cantidad, 'Tipo de ingreso': tipo_ingreso, 'Fecha': fecha}
    ingresos.append(nuevo_ingreso)
    sueldo += cantidad

    print(ingresos)
    print(f'\n${sueldo}')

def registro_gastos(cantidad, descripcion, fecha):
    global sueldo
    nuevo_gasto = {'Cantidad': cantidad, 'Descripcion de egreso': descripcion, 'Fecha': fecha}
    gastos.append(nuevo_gasto)

    sueldo -= cantidad

    print(gastos)
    print(f'\n${sueldo}')

def validar_num(lim_min, lim_max, mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= lim_min and numero <= lim_max: #Verifica que este en rango permitido
                return numero #Retorna el numero solo si es valido
            else:
                print(f"\nEl numero debe estar entre {lim_min} y {lim_max}. Intenta de nuevo!\n")
        except ValueError:
            print(" \nDebe ingresar un numero.\n ")



def menu():

    while True:

        print('\nMenu  principal \n_________________________________________')
        print( '''
        1. Registrar Ingreso.
        2. Registrar egreso.
        3. Ver saldo.
        4. Ver  historial
        5. Salir  ''')
        print('________________________________________')

        opcion = int(input('Ingresa la opcion que deseas realizar: '))

        if opcion == 1:
            total = int(input('Cantidad de ingreso: '))
            tipo = input('Procedencia del ingreso: ')
            dia = validar_num(1,31,'Digita dia del ingreso: ')
            mes = validar_num(1,12, 'Digita el mes del ingreso: ')
            año = validar_num(1000,2025, 'Ingresa el año del ingreso:  ')
            fecha= f'{dia}/{mes}/{año}'
            registrar_ingresos(total,tipo,fecha)


menu()"""