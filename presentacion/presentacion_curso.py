from prettytable import PrettyTable
from auxiliares import (
    mensaje_error,
    validar_largo_string,
    validar_numero
)
from negocio.negocio_curso import (
    lista_cursos,
    obtener_objeto_curso,
    crear_objeto_curso,
    actualizar_objeto_curso,
    eliminar_objeto_curso
)


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


def _pedir_texto_opcional(mensaje: str, largo: int = 0) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor == '':
            return ''
        if largo > 0:
            val_validado, msg = validar_largo_string(valor, largo)
            if val_validado == '':
                print(msg)
                continue
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


def mostrar_cursos():
    try:
        print(lista_cursos(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def agregar_curso():
    try:
        nombre = _pedir_texto('Ingrese nombre del curso: ', 30)
        nivel = _pedir_texto('Ingrese nivel del curso: ', 20)
        crear_objeto_curso(nombre, nivel)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_curso():
    try:
        mostrar_cursos()
        id_curso = _pedir_entero('Ingrese el ID del curso a modificar: ')
        encontrado = obtener_objeto_curso(id_curso)
        if encontrado:
            nombre = _pedir_texto_opcional('Nuevo nombre (o ENTER para conservar): ', 30)
            nivel = _pedir_texto_opcional('Nuevo nivel (o ENTER para conservar): ', 20)
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
