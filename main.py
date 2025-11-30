import json
from pathlib import Path
from datetime import datetime, date, time, timedelta
import Recursos
import Events
import funtion
import user
from sys import exit

name_user = ''
Recursos_disponibles = Recursos.Recursos_disponibles
###inicio del programa
while True:
    print('Hola, Bienvenido al Gestor de tareas para tu empresa de vehiculos.')
    print('1. Crearse una cuenta.')
    print('2. Cargar una cuenta.')
    print('3. Salir del Programa.')

    option = funtion.try_option(3)
    if option == 1:  ### Creacion de nueva cuenta
        while True:    
            print('Perfecto, entonces, cual sera tu nombre?')
            name_user = input()
            print('Y ahora establezcamos una contrasenna para asegurarnos de que nadie acceda a tu perfil.')
            passw = input()
            print(f'Tu perfil sera {name_user} con contrasenna {passw}, estas de acuerdo?')
            print('1. Si \n2. No \n3. Ir al menu principal.')
            option = funtion.try_option(3)
            if option == 1:
                print(f'Bienvenido {name_user}')
                print('Que deseas?')
                print('1. Agregar Eventos a tu agenda.')
                print('2. Eliminar Eventos de tu agenda.')
                print('3. Ver los Eventos agendados.')
                print('4. Ver los Recursos y su disponibilidad.')
                print('5. Salir al menu principal.')

                option = funtion.try_option(5)
                if option == 1: ### ver los eventos
                    print('Tienes para agregar:')
                    funtion.printeo_opciones_eventos()
                    option = funtion.try_option(11)
                    ### funcion qe dentro se encarge de llamar a otras funciones y que finalmente agrege ese evento si no incumple nada
                
                
                elif option == 2:
                    pass
                elif option == 3:
                    pass
                elif option == 4:
                    pass
                elif option == 5:
                    pass
            
            elif option == 2: ### Va a la sgt iteracion del bucle.
                continue
            elif option == 3: ### Rompe el bucle y vuelve al menu inicial.
                break


    elif option == 2:
        pass
    elif option == 3:
        print(f'Hasta luego {name_user}.')
        exit()