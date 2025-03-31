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
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])




class Registro(ABC):
    
    ingresos = 0
    egresos = 0
    saldo_total = 0
    historial = []

    def __init__(self, cantidad, tipo_registro):
        self.tipo = tipo_registro
        self.cantidad = cantidad
    
    @classmethod    
    def logestado(cls):
        mensaje = f'Ingresos totales: ${cls.ingresos}, Egresos totales: ${cls.egresos}'
        logging.info(mensaje)
        
    @abstractmethod
    def actualizar(self):
        pass


class Ingresos(Registro):
    
    def __init__(self, cantidad, tipo_registro):
        super().__init__(cantidad, tipo_registro)
        self.ingresos = []
        self.ingreso="Ingreso"
        
        
      
    
    def registrar_ingreso(self):
        
        if self.tipo not in ['sueldo', 'dividendos', 'independientes', 'otros']:
            raise ValueError(f'El tipo de ingreso {self.tipo} no es valido')
        if self.cantidad  <= 0 and self.cantidad != int:
            raise ValueError('La cantidad debe ser mayor a 0 y no puede ser letras')
        
           
        Registro.ingresos += self.cantidad 
        Registro.saldo_total += self.cantidad
        nuevo_ingreso = {'Cantidad': self.cantidad, 'Tipo de registro': self.tipo, 'Tipo':self.ingreso}        
        self.ingresos.append(nuevo_ingreso)
        Registro.historial.append(nuevo_ingreso) 
        
    
    def actualizar(self):
        logging.info(f'\nSu saldo actual es: ${Registro.saldo_total}')
                  
            
def historial_movimientos():
    print(f"{"Cantidad":<15} {"Tipo de registro":<20} {"Tipo":<15}")
    print("-------------------------------------------------")
    for historial in Registro.historial:
        print(f"{historial["Cantidad"]:<15} {historial["Tipo de registro"]:<20} {historial["Tipo"]:<15}")
               
        
class Gastos(Registro):

    def __init__(self, cantidad, tipo_registro):
        super().__init__(cantidad, tipo_registro)
        self.egresos = []
        self.egreso= "Egreso"
    
    
    
    def registrar_egreso(self):
            
            if self.tipo not in ['transporte', 'alimentacion', 'servicios', 'ocio', 'hogar', 'cuidado personal','otros']:
                raise ValueError(f'El tipo de egreso {self.tipo} no es valido')
            if self.cantidad  <= 0 and self.cantidad != int:
                raise ValueError('La cantidad debe ser mayor a 0 y no puede ser letras')
            if self.cantidad > Registro.saldo_total:
                raise ValueError('No cuentas con la  cantidad suficiente para este gasto.')            
            Registro.saldo_total -= self.cantidad
            Registro.egresos += self.cantidad
            nuevo_egreso = {'Cantidad': self.cantidad, 'Tipo de registro': self.tipo, 'Tipo':self.egreso} 
            self.egresos.append(nuevo_egreso)
            self.historial.append(nuevo_egreso)

            
            

    def actualizar(self):
        logging.info(f'\nSu saldo actual es: ${Registro.saldo_total}')
               
    


def menu():
    
    while True:
        print('\nMENU PRINCUPAL.')
        print('********************************')
        print('1. Ingresos')   
        print('2. Egresos')
        print('3. Historial Movimientos')
        print('4. Salir')
        print('********************************')
        
        try:
            opcion = input('Elige una opcion: ')
            if not opcion:
                raise ValueError('No puedes dejar espacios en blanco. Intenta de nuevo.')
            system('clear')
            if opcion == '1':
                try:    
                    ingreso = int(input('Cuanto es el ingreso:  '))
                    system('clear')
                    tipoIngreso = input('Cual es el tipo de ingreso:(Sueldo fijo, Dividendos, Independientes, Otros) ').lower()
                    system('clear')
                    ing = Ingresos(ingreso, tipoIngreso)
                    ing.registrar_ingreso()                
                    ing.actualizar()
                    Registro.logestado()
                except ValueError as e:
                    logging.error(f'ERROR: {e}')
                    
            elif  opcion == '2':
                try:
                    egreso = int(input('Cuanto dinero gasto:  '))
                    system('clear')
                    tipoEgreso = input('Cual es el tipo de egreso:(Transporte, alimentacion, servicios, ocio, hogar, cuidado personal,Otros) ').lower()
                    system('clear')
                    egr = Gastos(egreso, tipoEgreso)
                    egr.registrar_egreso()
                    egr.actualizar()
                    Registro.logestado()
                except ValueError as e:
                    logging.error(f'\nERROR: {e}')
            elif opcion == '3':
                system('clear')
                historial_movimientos()

            
            
            elif opcion == 4:
                logging.debug('Saliendo del programa.')
                break  
            else:
                logging.error('Opcion incorrecta')      
        
        except ValueError as e:
            system('clear')  
            logging.error(f'ERROR: {e}')
            
            
            
        except ValueError:
            system('clear')  
            logging.error('Opcion incorrecta. Intenta nuevamente.')
                  

menu()