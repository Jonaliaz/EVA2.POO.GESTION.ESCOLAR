from prettytable import PrettyTable
from negocio.negocio_registro_academico import lista_registros_academicos


def mostrar_registros_academicos():
    print("\n--- LISTADO DE REGISTROS ACADÉMICOS ---")
    print(lista_registros_academicos(PrettyTable()))
