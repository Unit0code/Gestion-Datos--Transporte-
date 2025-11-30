import json
from pathlib import Path
from datetime import datetime, date, time, timedelta


class User: ###Se inicializa el usuario una vez cargue el .json o cree una cuenta
    def __init__(self, name: str, passw: str, path : Path, events : list[Events]): 
        self.name = name
        self.passw = passw
        self.path = path
        self.events = events