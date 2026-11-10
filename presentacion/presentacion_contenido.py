from prettytable import PrettyTable
from negocio.negocio_contenido import lista_contenidos


def mostrar_contenidos():
    print(lista_contenidos(PrettyTable()))
