import json
from pathlib import Path
from datetime import datetime, date, time, timedelta


class User: ###Se inicializa el usuario una vez cargue el .json o cree una cuenta
    def __init__(self, name: str, passw: str, path : Path, events: list = []): 
        self.name = name
        self.passw = passw
        self.path = path
        self.events = events
    
    def __dict__(self):
        Data = { 'Nombre': self.name,
                 'Passw': self.passw,
                 'Path': self.path,
                 'Eventos': list(self.events)
                }
        return Data