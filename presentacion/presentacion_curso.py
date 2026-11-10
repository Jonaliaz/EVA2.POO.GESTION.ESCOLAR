from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio.negocio_curso import (
    lista_cursos,
    obtener_objeto_curso,
    crear_objeto_curso,
    actualizar_objeto_curso,
    eliminar_objeto_curso
)


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


def mostrar_cursos():
    try:
        print(lista_cursos(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def agregar_curso():
    try:
        nombre = _pedir_texto('Ingrese nombre del curso: ')
        nivel = _pedir_texto('Ingrese nivel del curso: ')
        crear_objeto_curso(nombre, nivel)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_curso():
    try:
        mostrar_cursos()
        id_curso = _pedir_entero('Ingrese el ID del curso a modificar: ')
        encontrado = obtener_objeto_curso(id_curso)
        if encontrado:
            nombre = input('Nuevo nombre (o ENTER para conservar): ').strip()
            nivel = input('Nuevo nivel (o ENTER para conservar): ').strip()
            actualizar_objeto_curso(nombre, nivel, encontrado)
        else:
            print('Curso no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def borrar_curso():
    try:
        mostrar_cursos()
        id_curso = _pedir_entero('Ingrese el ID del curso a eliminar: ')
        encontrado = obtener_objeto_curso(id_curso)
        if encontrado:
            eliminar_objeto_curso(encontrado)
        else:
            print('Curso no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')
