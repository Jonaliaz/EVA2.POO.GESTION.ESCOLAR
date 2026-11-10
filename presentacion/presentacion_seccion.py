from prettytable import PrettyTable
from negocio.negocio_seccion import (
    lista_secciones,
    crear_objeto_seccion
)
from presentacion.presentacion_curso import mostrar_cursos
from presentacion.presentacion_asignatura import mostrar_asignaturas


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


def mostrar_secciones():
    print(lista_secciones(PrettyTable()))


def agregar_seccion():
    numero = _pedir_texto('Ingrese número de sección (ej. 004): ')
    cupos = _pedir_entero('Ingrese cantidad de cupos: ')
    mostrar_cursos()
    id_curso = _pedir_entero('Ingrese ID del curso: ')
    mostrar_asignaturas()
    id_asignatura = _pedir_entero('Ingrese ID de la asignatura: ')
    crear_objeto_seccion(numero, cupos, id_curso, id_asignatura)
