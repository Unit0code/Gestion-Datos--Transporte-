import json
from pathlib import Path
from datetime import datetime, date, time, timedelta


###crear clase 'Vehiculo' y 'Conductor' derivadas de recursos class
class Events: ### Los eventos seran un tipo, con ciertos atributos y  ciertas restricciones.
    def __init__(self, fecha):
        self.fecha = datetime.strptime(fecha, '%d/%m/%Y---%H:%M')


class travel_Habana(Events): ### tipo evento de viajes a la habana.
    def __init__ (self, fecha, *Recursos):
        super().__init__( fecha)
        self.name = 'Viaje a la Habana'
        self.Restriction_hour = [ time(8), time(21) ] ###Restricciones de horario para iniciar el viaje.
        self.Duration = timedelta(hours = 2)  ### duracion del viaje
        self.Finish_date = self.Duration + self.fecha ###fecha de finalizacion
        self.Restriction_recursos = {} ### No pueden usarse para este evento.
        self.Restriction_recursos_pares = [('Suarez', 'Menedez')]  ###No pueden estar en el mismo Evento
        self.message = ['Cuando ambos se juntan, hacen destrozos por la Habana.'] ### Mensaje de las restricciones
        self.Needs = [ 'Conductor','Vehiculo']  ###lo necesario para iniciar el viaje.
        self.Recursos = Recursos
    
    def __dict__ (self):
        Data = {'Nombre': self.name,
                'Fecha inicio': datetime.strftime(self.fecha, '%d/%m/%Y - %H:%M'),
                'Fecha fin': datetime.strftime(self.Finish_date, '%d/%m/%Y - %H:%M'),
                'Recursos': self.Recursos
                 }
        return Data


class travel_Gto(Events): ### tipo evento de viajes a la Gto.
    def __init__ (self, fecha, *Recursos):
        super().__init__( fecha)
        self.name = 'Viaje a Guantanamo'
        self.Restriction_hour = [ time(8), time(21) ] ###Restricciones de horario para iniciar el viaje.
        self.Duration = timedelta(hours = 18)  ### duracion del viaje
        self.Finish_date = self.Duration + self.fecha ###fecha de finalizacion
        self.Restriction_recursos = {'Juan' : 'No se le dan los viajes largos.'} ### No pueden usarse para este evento.
        self.Restriction_recursos_pares = [('Pedro', 'Rigoberto')] ###No pueden estar en el mismo Evento
        self.message = ['La ultima vez que estuvieron esos locos juntos, chocaron.'] ### Mensaje de las restricciones
        self.Needs = [ 'Conductor','Vehiculo']  ###lo necesario para iniciar el viaje.
        self.Recursos = Recursos
    
    def __dict__ (self):
        Data = {'Nombre': self.name,
                'Fecha inicio': datetime.strftime(self.fecha, '%d/%m/%Y - %H:%M'),
                'Fecha fin': datetime.strftime(self.Finish_date, '%d/%m/%Y - %H:%M'),
                'Recursos': self.Recursos
                 }
        return Data
    


class User: ###Se inicializa el usuario una vez cargue el .json o cree una cuenta
    def __init__(self, name: str, passw: str, path : Path, events : list[Events]): 
        self.name = name
        self.passw = passw
        self.path = path
        self.events = events

c1 = travel_Habana('10/10/2005---20:10', 'jamon' )
c2 = travel_Gto('10/12/2007---20:10')

print(c1.__dict__())
print(c2.__dict__())
