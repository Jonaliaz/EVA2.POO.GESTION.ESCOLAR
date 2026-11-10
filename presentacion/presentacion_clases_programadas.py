from prettytable import PrettyTable
from negocio.negocio_clases_programadas import (
    lista_clases_programadas,
    disponibilidad_sala
)


def mostrar_clases_y_sala():
    print(lista_clases_programadas(PrettyTable()))
    sala = input('Si desea verificar disponibilidad de una sala, escriba su nombre (o ENTER para omitir): ').strip()
    if sala != '':
        disponible = disponibilidad_sala(sala)
        print(f"¿La sala '{sala}' está disponible?: {'Sí' if disponible else 'No (Ya tiene clases programadas)'}\n")
