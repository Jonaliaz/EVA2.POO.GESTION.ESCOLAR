from prettytable import PrettyTable
from negocio.negocio_asignatura import (
    lista_asignaturas,
    crear_objeto_asignatura
)
from presentacion.presentacion_profesor import mostrar_profesores


def _pedir_texto(mensaje: str) -> str:
    valor = ''
    while valor == '':
        valor = input(mensaje).strip()
        if valor == '':
            print("El campo no puede estar vacío.")
    return valor


def _pedir_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida: debe ingresar un número entero.")


def mostrar_asignaturas():
    print(lista_asignaturas(PrettyTable()))


def agregar_asignatura():
    nombre = _pedir_texto('Ingrese nombre de la asignatura: ')
    descripcion = _pedir_texto('Ingrese descripción: ')
    mostrar_profesores()
    id_profesor = _pedir_entero('Ingrese ID del profesor: ')
    crear_objeto_asignatura(nombre, descripcion, id_profesor)
