from collections.abc import Callable
from prettytable import PrettyTable
from auxiliares import (
    nombre_app,
    version_app,
    opcion_volver,
    opcion_invalida,
    mensaje_error,
    menu_superior,
    menu_alumnos,
    menu_profesores,
    menu_cursos,
    menu_academico
)
from datos.repositorios.repo_escuela import (
    obtener_alumno,
    eliminar_alumno,
    asignar_curso,
    obtener_profesor,
    eliminar_profesor,
    obtener_curso,
    eliminar_curso,
    verificar_disponibilidad_de_sala
)
from negocio.gestion_escolar import (
    lista_alumnos,
    crear_objeto_alumno,
    actualizar_objeto_alumno,
    lista_profesores,
    crear_objeto_profesor,
    actualizar_objeto_profesor,
    lista_cursos,
    crear_objeto_curso,
    actualizar_objeto_curso,
    lista_secciones,
    crear_objeto_seccion,
    lista_apoderados,
    crear_objeto_apoderado,
    lista_asignaturas,
    crear_objeto_asignatura,
    lista_contenidos,
    lista_evaluaciones,
    lista_notas,
    crear_objeto_nota,
    lista_clases_programadas,
    lista_asistencias,
    lista_registros_academicos
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


def _pedir_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida: debe ingresar un número decimal (ej. 6.5).")



def mostrar_alumnos():
    try:
        print(lista_alumnos(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def agregar_alumno():
    try:
        nombre = _pedir_texto('Ingrese nombre del alumno: ')
        correo = _pedir_texto('Ingrese correo del alumno: ')
        telefono = _pedir_texto('Ingrese teléfono del alumno: ')
        mostrar_cursos()
        id_curso = _pedir_entero('Ingrese ID del curso: ')
        mostrar_secciones()
        id_seccion = _pedir_entero('Ingrese ID de la sección: ')
        mostrar_apoderados()
        id_apoderado = _pedir_entero('Ingrese ID del apoderado: ')
        crear_objeto_alumno(nombre, correo, telefono, id_seccion, id_curso, id_apoderado)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_alumno():
    try:
        mostrar_alumnos()
        id_alumno = _pedir_entero('Ingrese el ID del alumno a modificar: ')
        encontrado = obtener_alumno(id_alumno)
        if encontrado:
            print(f'\nAlumno encontrado: {encontrado.nombre}')
            nombre = input('Nuevo nombre (o ENTER para conservar): ').strip()
            correo = input('Nuevo correo (o ENTER para conservar): ').strip()
            telefono = input('Nuevo teléfono (o ENTER para conservar): ').strip()
            id_seccion = input('Nuevo ID sección (o ENTER para conservar): ').strip()
            id_curso = input('Nuevo ID curso (o ENTER para conservar): ').strip()
            id_apoderado = input('Nuevo ID apoderado (o ENTER para conservar): ').strip()
            actualizar_objeto_alumno(nombre, correo, telefono, id_seccion, id_curso, id_apoderado, encontrado)
        else:
            print('Alumno no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def borrar_alumno():
    try:
        mostrar_alumnos()
        id_alumno = _pedir_entero('Ingrese el ID del alumno a eliminar: ')
        encontrado = obtener_alumno(id_alumno)
        if encontrado:
            eliminar_alumno(encontrado)
        else:
            print('Alumno no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def cambiar_curso_alumno():
    try:
        mostrar_alumnos()
        id_alumno = _pedir_entero('Ingrese el ID del alumno: ')
        alumno = obtener_alumno(id_alumno)
        mostrar_cursos()
        id_curso = _pedir_entero('Ingrese el ID del nuevo curso a asignar: ')
        curso = obtener_curso(id_curso)
        if alumno and curso:
            asignar_curso(alumno, curso)
        else:
            print('Alumno o Curso no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')



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
        encontrado = obtener_profesor(id_profesor)
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
        encontrado = obtener_profesor(id_profesor)
        if encontrado:
            eliminar_profesor(encontrado)
        else:
            print('Profesor no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')



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
        encontrado = obtener_curso(id_curso)
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
        encontrado = obtener_curso(id_curso)
        if encontrado:
            eliminar_curso(encontrado)
        else:
            print('Curso no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


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



def mostrar_apoderados():
    print(lista_apoderados(PrettyTable()))


def agregar_apoderado():
    nombre = _pedir_texto('Ingrese nombre del apoderado: ')
    correo = _pedir_texto('Ingrese correo del apoderado: ')
    telefono = _pedir_texto('Ingrese teléfono del apoderado: ')
    crear_objeto_apoderado(nombre, correo, telefono)


def mostrar_asignaturas():
    print(lista_asignaturas(PrettyTable()))


def agregar_asignatura():
    nombre = _pedir_texto('Ingrese nombre de la asignatura: ')
    descripcion = _pedir_texto('Ingrese descripción: ')
    mostrar_profesores()
    id_profesor = _pedir_entero('Ingrese ID del profesor: ')
    crear_objeto_asignatura(nombre, descripcion, id_profesor)


def mostrar_contenidos():
    print(lista_contenidos(PrettyTable()))


def mostrar_evaluaciones():
    print(lista_evaluaciones(PrettyTable()))


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


def mostrar_clases_y_sala():
    print(lista_clases_programadas(PrettyTable()))
    sala = input('Si desea verificar disponibilidad de una sala, escriba su nombre (o ENTER para omitir): ').strip()
    if sala != '':
        disponible = verificar_disponibilidad_de_sala(sala)
        print(f"¿La sala '{sala}' está disponible?: {'Sí' if disponible else 'No (Ya tiene clases programadas)'}\n")


def mostrar_asistencias_y_registros():
    print("\n--- LISTADO DE ASISTENCIAS ---")
    print(lista_asistencias(PrettyTable()))
    print("\n--- LISTADO DE REGISTROS ACADÉMICOS ---")
    print(lista_registros_academicos(PrettyTable()))



def _ejecutar_menu(
    opciones: dict[str, str],
    acciones: dict[str, Callable[[], None]],
    mensaje_salida: str = opcion_volver,
) -> None:
    while True:
        print()
        for clave, valor in opciones.items():
            print(f'[{clave}] - {valor}')

        opcion = input('Ingrese su opción: ').strip()
        if opcion not in opciones:
            print(opcion_invalida)
        elif opcion == '0':
            print(mensaje_salida)
            return
        elif opcion in acciones:
            acciones[opcion]()
        else:
            print('Esta opción aún no está implementada.\n')


def _menu_alumnos() -> None:
    _ejecutar_menu(menu_alumnos, {
        '1': mostrar_alumnos,
        '2': agregar_alumno,
        '3': modificar_alumno,
        '4': borrar_alumno,
        '5': cambiar_curso_alumno
    })


def _menu_profesores() -> None:
    _ejecutar_menu(menu_profesores, {
        '1': mostrar_profesores,
        '2': agregar_profesor,
        '3': modificar_profesor,
        '4': borrar_profesor
    })


def _menu_cursos() -> None:
    _ejecutar_menu(menu_cursos, {
        '1': mostrar_cursos,
        '2': agregar_curso,
        '3': modificar_curso,
        '4': borrar_curso,
        '5': mostrar_secciones,
        '6': agregar_seccion
    })


def _menu_academico() -> None:
    _ejecutar_menu(menu_academico, {
        '1': mostrar_apoderados,
        '2': agregar_apoderado,
        '3': mostrar_asignaturas,
        '4': agregar_asignatura,
        '5': mostrar_contenidos,
        '6': mostrar_evaluaciones,
        '7': mostrar_notas,
        '8': agregar_nota,
        '9': mostrar_clases_y_sala,
        '10': mostrar_asistencias_y_registros
    })


def menu_principal() -> None:
    print(f'{nombre_app} v{version_app}')
    print('=' * (len(nombre_app) + len(version_app) + 2))

    _ejecutar_menu(
        menu_superior,
        {
            '1': _menu_alumnos,
            '2': _menu_profesores,
            '3': _menu_cursos,
            '4': _menu_academico,
        },
        'Saliendo...\n',
    )