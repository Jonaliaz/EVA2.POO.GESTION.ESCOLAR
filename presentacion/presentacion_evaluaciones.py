from prettytable import PrettyTable
from negocio.negocio_evaluaciones import lista_evaluaciones


def mostrar_evaluaciones():
    print(lista_evaluaciones(PrettyTable()))
