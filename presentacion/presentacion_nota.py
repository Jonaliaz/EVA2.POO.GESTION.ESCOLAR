from prettytable import PrettyTable
from auxiliares import (
    validar_numero,
    validar_fecha
)
from negocio.negocio_nota import (
    lista_notas,
    crear_objeto_nota
)
from presentacion.presentacion_alumno import mostrar_alumnos
from presentacion.presentacion_evaluaciones import mostrar_evaluaciones


def _pedir_entero(mensaje: str) -> int:
    while True:
        entrada = input(mensaje).strip()
        if entrada == '':
            print("El campo no puede estar vacío.")
            continue
        numero, msg = validar_numero(entrada)
        if numero == 0 and entrada != '0':
            print(msg)
        else:
            return numero


def _pedir_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida: debe ingresar un número decimal (ej. 6.5).")


def _pedir_fecha(mensaje: str):
    while True:
        entrada = input(mensaje).strip()
        if entrada == '':
            print("El campo no puede estar vacío.")
            continue
        fecha, msg = validar_fecha(entrada)
        print(msg)
        if fecha != '':
            return fecha.date()


def mostrar_notas():
    print(lista_notas(PrettyTable()))


def agregar_nota():
    mostrar_alumnos()
    id_alumno = _pedir_entero('Ingrese ID del alumno: ')
    mostrar_evaluaciones()
    id_evaluaciones = _pedir_entero('Ingrese ID de la evaluación: ')
    calificacion = _pedir_float('Ingrese calificación (ej. 6.5): ')
    fecha = _pedir_fecha('Ingrese fecha (DD/MM/YYYY): ')
    crear_objeto_nota(calificacion, fecha, id_alumno, id_evaluaciones)
