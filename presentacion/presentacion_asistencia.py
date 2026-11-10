from prettytable import PrettyTable
from negocio.negocio_asistencia import lista_asistencias
from presentacion.presentacion_registro_academico import mostrar_registros_academicos


def mostrar_asistencias():
    print("\n--- LISTADO DE ASISTENCIAS ---")
    print(lista_asistencias(PrettyTable()))


def mostrar_asistencias_y_registros():
    mostrar_asistencias()
    mostrar_registros_academicos()
