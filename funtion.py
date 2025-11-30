import json
from pathlib import Path
from datetime import datetime, date, time, timedelta
from user import User
from Recursos import Recurso
import Events


def guardar_json (usuario : User): ###guardar los avances en un json con un path 'nombre_user'.json
    data = usuario.__dict__()
    for llave, valor in data.items(): ###convertir todos los tipos en un dict para ser guardados.
        if llave == 'Eventos':
            for idx, eventos in enumerate(valor): ###Itero en los eventos 
                for idc, recursos_evento in enumerate(eventos.Recursos): ###itero en los recursos de ese evento
                    eventos.Recursos[idc] = recursos_evento.__dict__()   ###cada evento lo vuelvo un dict
                valor[idx] = eventos.__dict__() ### y finalizo ese evento volviendolo un dict tambien

    data = json.dumps(data)  ###lo vuelvo un tipo json
    path_user = Path(f'{usuario.path}.json')  ### inicializo una instancia Path 
    path_user.write_text(data)  ### y escribo en el archivo con ese path
    return 'Hecho.'

def cargar_json (path : str):
    path_user = Path(f'{path}.json')
    
    try:
        data_user = path_user.read_text()
    except FileNotFoundError:
        print(f"El archivo con direccion {path_user} no existe.") ###Si el archivo no existe
        return False
    else:
        data_user = json.loads(data_user)
        data_user = inicializar_obj_cargados(data_user) ### se inicializan los tipos recursos y datetime en cada event
        data_user = inicializar_eventos(data_user) ### se inicializan los eventos
        user = inicializar_user(data_user, path) ### se inicializa el usuario
        return user
    ### llamar a todas las funciones de iniacializacion
    
def inicializar_obj_cargados (data_user): ### cuando cargue el archivo, se deben inicializar todos los tipos
    Eventos = data_user.get('Eventos', False)
    if not Eventos: ###si no existe la llave
        return False
    for idx, evento_p in enumerate(Eventos): ### por cada evento
        for llave, valor in evento_p.items(): ### vere las caracteristicas de dicho evento
            if llave == 'Recursos':  ### instancias recursos
                for idc, recurso in enumerate(valor): ### por cada recurso
                    nombre = recurso['Nombre']
                    categoria = recurso['Categoria']
                    estado = recurso['Estado']
                    recurso_obj = Recurso(nombre, categoria, estado) ### creacion de las inst recursos
                    valor[idc] = recurso_obj
    data_user['Eventos'] = Eventos
    return data_user  ### devuelve los eventos con todos sus tipos inicializados, exceptuando el mismo Evento

def inicializar_eventos (data_user):
    Eventos = data_user.get('Eventos', False)
    if not Eventos:
        return False
    for idx, evento_p in enumerate(Eventos): ### tomo sus atributos
        nombre = evento_p['Nombre']
        fecha = evento_p['Fecha inicio']
        recursos = evento_p['Recursos']
        
        if nombre == 'Viaje a la Habana':   ### dependiendo del nombre inicializo la instancia Evento(tipo especif)
            evento_p = Events.travel_Habana(fecha, *recursos)
            Eventos[idx] = evento_p
        
        elif nombre == 'Viaje a Guantanamo':
            evento_p = Events.travel_Gto(fecha, *recursos)
            Eventos[idx] = evento_p
        
        elif nombre == 'Viaje a Santiago de Cuba':
            evento_p = Events.travel_Stgo(fecha, *recursos)
            Eventos[idx] = evento_p
        
        elif nombre == 'Viaje a Camaguey':
            evento_p = Events.travel_Camaguey(fecha, *recursos)
            Eventos[idx] = evento_p

        elif nombre == 'Viaje a Las Tunas':
            evento_p = Events.travel_Las_Tunas(fecha, *recursos)
            Eventos[idx] = evento_p
        
        elif nombre == 'Viaje a Las Villas':
            evento_p = Events.travel_Las_Villas(fecha, *recursos)
            Eventos[idx] = evento_p
        
        elif nombre == 'Viaje a Pinar del Rio': ###
            evento_p = Events.travel_Pinar_Rio(fecha, *recursos)
            Eventos[idx] = evento_p
        
        elif nombre == 'Viaje a Matanzas':
            evento_p = Events.travel_Mtz(fecha, *recursos)
            Eventos[idx] = evento_p
        
        elif nombre == 'Viaje a Cienfuegos':
            evento_p = Events.travel_Cienfuegos(fecha, *recursos)
            Eventos[idx] = evento_p

        elif nombre == 'Mantenimiento de Vehiculos':
            evento_p = Events.Mantenimiento_Vehiculos(fecha, *recursos)
            Eventos[idx] = evento_p
        
        elif nombre == 'Boteo en la Habana':
            evento_p = Events.Botear_Habana(fecha, *recursos)
            Eventos[idx] = evento_p
    data_user['Eventos'] = Eventos
    return data_user

def inicializar_user (data_user, path):
    nombre = data_user['Nombre']
    passw = data_user['Passw']
    path_r = path
    eventos = data_user['Eventos']
    user = User(nombre, passw, path_r, eventos)
    return user
            


