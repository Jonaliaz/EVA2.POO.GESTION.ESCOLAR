from collections.abc import Callable
from auxiliares import (
    nombre_app,
    version_app,
    opcion_volver,
    opcion_invalida,
    menu_superior,
    menu_alumnos,
    menu_profesores,
    menu_cursos,
    menu_academico,
    menu_usuarios
)
from presentacion.presentacion_alumno import (
    mostrar_alumnos,
    agregar_alumno,
    modificar_alumno,
    borrar_alumno,
    cambiar_curso_alumno
)
from presentacion.presentacion_profesor import (
    mostrar_profesores,
    agregar_profesor,
    modificar_profesor,
    borrar_profesor
)
from presentacion.presentacion_curso import (
    mostrar_cursos,
    agregar_curso,
    modificar_curso,
    borrar_curso
)
from presentacion.presentacion_seccion import (
    mostrar_secciones,
    agregar_seccion
)
from presentacion.presentacion_apoderado import (
    mostrar_apoderados,
    agregar_apoderado
)
from presentacion.presentacion_asignatura import (
    mostrar_asignaturas,
    agregar_asignatura
)
from presentacion.presentacion_contenido import mostrar_contenidos
from presentacion.presentacion_evaluaciones import mostrar_evaluaciones
from presentacion.presentacion_nota import (
    mostrar_notas,
    agregar_nota
)
from presentacion.presentacion_clases_programadas import mostrar_clases_y_sala
from presentacion.presentacion_asistencia import mostrar_asistencias_y_registros
from presentacion.presentacion_usuario import (
    mostrar_usuarios,
    mostrar_usuarios_habilitados,
    mostrar_usuarios_deshabilitados,
    agregar_usuario,
    modificar_usuario,
    borrar_usuario
)


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


def _menu_usuarios() -> None:
    _ejecutar_menu(menu_usuarios, {
        '1': mostrar_usuarios,
        '2': mostrar_usuarios_habilitados,
        '3': mostrar_usuarios_deshabilitados,
        '4': agregar_usuario,
        '5': modificar_usuario,
        '6': borrar_usuario
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
            '5': _menu_usuarios,
        },
        'Saliendo...\n',
    )
