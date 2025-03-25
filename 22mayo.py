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

"""ingresos = []
historial = []
balance = []"""


class Registro(ABC):
    

    def __init__(self, tipo_registro, cantidad):
        self.tipo = tipo_registro
        self.cantidad = cantidad
        self.historial = []

        
    @abstractmethod
    def actualizar(self):
        pass


class Ingresos(Registro):
    
    def __init__(self, tipo_registro, cantidad):
        super().__init__(tipo_registro, cantidad)
        self.ingresos = []

    def __str__(self):
        return f'Cantidad ingresos: {self.cantidad}, Tipo: {self.tipo}'
    
    def regitrar_ingreso(self):
        
        while True:
            ingreso = int(input('Cuanto deseas depositar:  '))
            tipoIngreso = input('Cual es el tipo de ingreso:(Sueldo fijo, Dividendos, Independientes, Otros) ').lower()
            if tipoIngreso not in ['sueldo fijo', 'dividendos', 'independientes', 'otros']:
                raise ValueError(f'El tipo de ingreso {tipoIngreso} no es valido')
            if ingreso > 0:
                raise ValueError('La cantidad debe ser mayor a 0')
            
            self.cantidad += ingreso
                


    def actualizar(self):
        nuevo_ingreso = {'Cantidad': self.cantidad, 'Tipo de registro': self.tipo}        
        self.ingresos.append(nuevo_ingreso)
        self.historial.append(nuevo_ingreso)
        
class Gastos(Registro):

    def __init__(self, tipo_registro, cantidad):
        super().__init__(tipo_registro, cantidad)
        self.egresos = []

    def __str__(self):
        return f'Cantidad egresos: {self.cantidad}, Tipo: {self.tipo}'
    
    def regitrar_ingreso(self):
        
        while True:
            ingreso = int(input('Cuanto deseas depositar:  '))
            tipoIngreso = input('Cual es el tipo de ingreso:(Sueldo fijo, Dividendos, Independientes, Otros) ').lower()
            if tipoIngreso not in ['sueldo fijo', 'dividendos', 'independientes', 'otros']:
                raise ValueError(f'El tipo de ingreso {tipoIngreso} no es valido')
            if ingreso > 0:
                raise ValueError('La cantidad debe ser mayor a 0')
            
            self.cantidad += ingreso





   






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