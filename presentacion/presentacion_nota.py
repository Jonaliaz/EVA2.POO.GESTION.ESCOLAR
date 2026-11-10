from prettytable import PrettyTable
from negocio.negocio_nota import (
    lista_notas,
    crear_objeto_nota
)
from presentacion.presentacion_alumno import mostrar_alumnos
from presentacion.presentacion_evaluaciones import mostrar_evaluaciones


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


def _pedir_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida: debe ingresar un número decimal (ej. 6.5).")


def mostrar_notas():
    print(lista_notas(PrettyTable()))


def agregar_nota():
    mostrar_alumnos()
    id_alumno = _pedir_entero('Ingrese ID del alumno: ')
    mostrar_evaluaciones()
    id_evaluaciones = _pedir_entero('Ingrese ID de la evaluación: ')
    calificacion = _pedir_float('Ingrese calificación (ej. 6.5): ')
    fecha = _pedir_texto('Ingrese fecha (YYYY-MM-DD): ')
    crear_objeto_nota(calificacion, fecha, id_alumno, id_evaluaciones)
