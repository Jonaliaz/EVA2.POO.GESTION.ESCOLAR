from prettytable import PrettyTable
from auxiliares import (
    validar_largo_string,
    validar_numero
)
from negocio.negocio_seccion import (
    lista_secciones,
    crear_objeto_seccion
)
from presentacion.presentacion_curso import mostrar_cursos
from presentacion.presentacion_asignatura import mostrar_asignaturas


def _pedir_texto(mensaje: str, largo: int = 0) -> str:
    valor = ''
    while valor == '':
        valor = input(mensaje).strip()
        if valor == '':
            print("El campo no puede estar vacío.")
        elif largo > 0:
            valor, msg = validar_largo_string(valor, largo)
            if valor == '':
                print(msg)
    return valor


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


def mostrar_secciones():
    print(lista_secciones(PrettyTable()))


def agregar_seccion():
    numero = _pedir_texto('Ingrese número de sección (ej. 004): ', 35)
    cupos = _pedir_entero('Ingrese cantidad de cupos: ')
    mostrar_cursos()
    id_curso = _pedir_entero('Ingrese ID del curso: ')
    mostrar_asignaturas()
    id_asignatura = _pedir_entero('Ingrese ID de la asignatura: ')
    crear_objeto_seccion(numero, cupos, id_curso, id_asignatura)
