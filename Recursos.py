import json
from pathlib import Path
from datetime import datetime, date, time, timedelta


class Recurso:
    def __init__(self, nombre:str , categoria: str, estado: str = 'None'):
        self.nombre = nombre
        self.categoria = categoria
        self.estado = estado
    
    def __dict__(self):
        Data = { 'Nombre': self.nombre,
                 'Categoria': self.categoria,
                 'Estado': self.estado
                }
        return Data
    
    def __repr__ (self):
        Data = { 'Nombre': self.nombre,
                 'Categoria': self.categoria,
                 'Estado': self.estado
                }
        return f'{Data}'

### Se inicializaran recursos siempre que empiece el programa
### y dependiendo que cuales tenga el usuario se eliminaran dichas instancias

transtur1 = Recurso('Transtur1', 'Vehiculo', 'OK')
transtur2 = Recurso('Transtur2', 'Vehiculo', 'OK')
camion1= Recurso('Camion1', 'Vehiculo', 'OK')
camion2 = Recurso('Camion2', 'Vehiculo', 'OK')
chofer_juan = Recurso('Juan', 'Conductor')
chofer_pedro = Recurso('Pedro', 'Conductor')
chofer_rigoberto = Recurso('Rigoberto', 'Conductor')
chofer_menendez = Recurso('Menendez', 'Conductor')
mecanico_suarez = Recurso('Suarez', 'Mecanico')
mecanico_jose = Recurso('Jose', 'Mecanico')
admin_marlon = Recurso('Marlon', 'Admin')
admin_diego = Recurso('Diego', 'Admin')
guias_federico = Recurso('Federico', 'Guia')
guia_phineas = Recurso('Phineas', 'Guia')


Recursos_disponibles = [ ###Todas las instancias inicializadas arriba
    transtur1, transtur2, camion1, camion2,
    chofer_juan,chofer_menendez, chofer_pedro,
    chofer_rigoberto, mecanico_jose, mecanico_suarez,
    admin_marlon, admin_diego, guias_federico, guia_phineas
                        ]