from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio.negocio_profesor import (
    lista_profesores,
    obtener_objeto_profesor,
    crear_objeto_profesor,
    actualizar_objeto_profesor,
    eliminar_objeto_profesor
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


def mostrar_profesores():
    try:
        print(lista_profesores(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def agregar_profesor():
    try:
        nombre = _pedir_texto('Ingrese nombre del profesor: ')
        correo = _pedir_texto('Ingrese correo del profesor: ')
        telefono = _pedir_texto('Ingrese teléfono del profesor: ')
        crear_objeto_profesor(nombre, correo, telefono)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_profesor():
    try:
        mostrar_profesores()
        id_profesor = _pedir_entero('Ingrese el ID del profesor a modificar: ')
        encontrado = obtener_objeto_profesor(id_profesor)
        if encontrado:
            print(f'\nProfesor encontrado: {encontrado.nombre}')
            nombre = input('Nuevo nombre (o ENTER para conservar): ').strip()
            correo = input('Nuevo correo (o ENTER para conservar): ').strip()
            telefono = input('Nuevo teléfono (o ENTER para conservar): ').strip()
            actualizar_objeto_profesor(nombre, correo, telefono, encontrado)
        else:
            print('Profesor no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def borrar_profesor():
    try:
        mostrar_profesores()
        id_profesor = _pedir_entero('Ingrese el ID del profesor a eliminar: ')
        encontrado = obtener_objeto_profesor(id_profesor)
        if encontrado:
            eliminar_objeto_profesor(encontrado)
        else:
            print('Profesor no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')
