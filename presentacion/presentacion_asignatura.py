from prettytable import PrettyTable
from auxiliares import (
    validar_largo_string,
    validar_numero
)
from negocio.negocio_asignatura import (
    lista_asignaturas,
    crear_objeto_asignatura
)
from presentacion.presentacion_profesor import mostrar_profesores


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


def mostrar_asignaturas():
    print(lista_asignaturas(PrettyTable()))


def agregar_asignatura():
    nombre = _pedir_texto('Ingrese nombre de la asignatura: ', 40)
    descripcion = _pedir_texto('Ingrese descripción: ', 100)
    mostrar_profesores()
    id_profesor = _pedir_entero('Ingrese ID del profesor: ')
    crear_objeto_asignatura(nombre, descripcion, id_profesor)
