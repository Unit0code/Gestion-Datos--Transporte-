import json
from pathlib import Path
from datetime import datetime, date, timedelta
import Recursos
import Events
import Jsons
from user import User
from sys import exit
import time
from miscelaneo import clear, try_option

def eliminar_eventos (user: User): ###eliminara un evento de los agregados en el atributo eventos del user
    clear()
    for idx, evento in enumerate(user.events):
        print(f'{idx + 1}. {evento.name}:    fecha de inicio -> {evento.fecha} \nfecha de finalizacion -> {evento.Finish_date}')
        print('Recursos:')
        for idx, recurso in enumerate(evento.Recursos):
            print(f'  {idx + 1}. {recurso.nombre}:   categoria -> {recurso.categoria}, estado -> {recurso.estado}')
        print('')
    if not user.events:
        print('No existen eventos que eliminar.')
        return user
    
    print('Cual desea eliminar?')
    option = try_option(len(user.events))
    print(f'Deseas eliminar {user.events[option - 1].name}??')
    print('1. Si.')
    print('2. No')
    option = try_option(2) 
    if option == 1:
        del user.events[option - 1]
        clear()                                                                
        print('Ha sido eliminado el evento.')                                             
        return user
    else:
        clear()
        print('Ok. Entonces volvamos.')
        return user

def mostras_eventos(user: User):
    clear()
    for idx, evento in enumerate(user.events):
        print(f'{idx + 1}. {evento.name}:    fecha de inicio -> {evento.fecha} \nfecha de finalizacion -> {evento.Finish_date}')
        print('Recursos:')
        for idx, recurso in enumerate(evento.Recursos):
            print(f'   {idx + 1}. {recurso.nombre}:   categoria -> {recurso.categoria}, estado -> {recurso.estado}')
        print('')
    if not user.events:
        print('No hay eventos por el momento')