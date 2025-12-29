import json
from pathlib import Path
from datetime import datetime, date, timedelta
from user import User
from Recursos import Recurso
import Events
import time
import os

def recomendador_cuentas (): ### lee los archivos en la carpeta del proyecto y ve cuales son los .json 
    ruta_relativa = './'
    contenido = os.listdir(ruta_relativa)
    archivos_json = []

    clear()
    for nombre in contenido:
        if nombre.endswith('.json'):
            archivos_json.append(nombre)
    if not archivos_json:
        print('No hay cuentas existentes.')
    else:
        print('Posibles cuentas:')
        for nombre in archivos_json:
            print(nombre)
        print('')

def verificador_passw(passw : str, user:User):
    return passw == user.passw         ### verifica si la contrasenna es igual.

def try_option (max, min = 1): ###Para los errores que pudiera generar el int(input())
    while True:
        try:
            option = int(input())
            if  option > max or option < min:
                print('El valor no esta en el intervalo esperado.\nVuelva a introducirlo.')
                continue
            return option
        except Exception:
            print('El valor introducido ha generado un error.\nVuelva a introducirlo.')

def clear(): ###limpia la pantalla
    time.sleep(0.2)
    os.system('cls')

def barra_de_progreso(): ###por hacer algo chulo
    a = '.'
    for i in range(2):
        for j in range(7):
            print(a * j, end = '\r')
            time.sleep(0.3)
        print('           ', end= '\r')

def mostrar_recursos(recursos_disponibles, user: User):
    clear()
    
    for idx, recurso in enumerate(recursos_disponibles):  ### veo todos los recursos
        print(f'{idx + 1}. {recurso.nombre}:   categoria -> {recurso.categoria}, estado -> {recurso.estado}')
        ver, horarios = check_uso(recurso, user.events)
        if ver:
            print('El recurso no estara disponible en los horarios: ')
            for hora_i, hora_f in horarios:
                print(f'**{hora_i}   <->   **{hora_f}   ')
        print('')
    print('')

def check_uso(recurso, eventos: list):
    horarios = []
    if not eventos:
        return False, False ### lista vacia
    else:
        for evento in eventos:  ### veo en cada evento los recursos que estan en uso en algun horario
            for recurso_uso in evento.Recursos:
                if recurso_uso.nombre == recurso.nombre: ### analizo si el recurso que estoy analizando esta dentro de algun evento
                    horarios.append((evento.fecha, evento.Finish_date)) ### tomo sus horarios.
        if not horarios:
            return False, False ### por si los eventos no son vacios pero el recurso no se usa
        return True, horarios 

def verificador_estado_eventos (user: User):
    clear()
    eventos_expirados = []
    fecha_hoy = datetime.today() ###creo la fecha de ese momento

    for idx, eventos in enumerate(user.events):  
        if eventos.Finish_date < fecha_hoy: ###chequeo si la fecha ya es pasada
            eventos_expirados.append(eventos) ###La agrego a eventos expirados
            print(f'Expiro {eventos.name}.')
    
    if not eventos_expirados: ###si la lista esta vacia solo regresara False
        print('No ha expirado ningun evento.')
        return user
    
    for evento in eventos_expirados:
        idx = user.events.index(evento)
        del user.events[idx] ### lo elimino de los atributos del usuario
    return user