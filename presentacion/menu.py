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
    menu_academico,
    menu_usuarios
)
from negocio.negocio_alumno import (
    lista_alumnos,
    obtener_objeto_alumno,
    crear_objeto_alumno,
    actualizar_objeto_alumno,
    eliminar_objeto_alumno,
    asignar_curso_alumno
)
from negocio.negocio_profesor import (
    lista_profesores,
    obtener_objeto_profesor,
    crear_objeto_profesor,
    actualizar_objeto_profesor,
    eliminar_objeto_profesor
)
from negocio.negocio_curso import (
    lista_cursos,
    obtener_objeto_curso,
    crear_objeto_curso,
    actualizar_objeto_curso,
    eliminar_objeto_curso
)
from negocio.negocio_seccion import (
    lista_secciones,
    crear_objeto_seccion
)
from negocio.negocio_apoderado import (
    lista_apoderados,
    crear_objeto_apoderado,
    obtener_objeto_apoderado
)
from negocio.negocio_asignatura import (
    lista_asignaturas,
    crear_objeto_asignatura
)
from negocio.negocio_contenido import lista_contenidos
from negocio.negocio_evaluaciones import lista_evaluaciones
from negocio.negocio_nota import (
    lista_notas,
    crear_objeto_nota
)
from negocio.negocio_clases_programadas import (
    lista_clases_programadas,
    disponibilidad_sala
)
from negocio.negocio_asistencia import lista_asistencias
from negocio.negocio_registro_academico import lista_registros_academicos
from negocio.negocio_usuarios import (
    lista_usuarios,
    lista_usuarios_habilitados,
    lista_usuarios_inactivos,
    obtener_objeto_usuario,
    crear_objeto_usuario,
    actualizar_objeto_usuario,
    eliminar_objeto_usuario
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


#confirmacion para los id de los usuarios
def agregar_alumno():
    try:
        nombre = _pedir_texto('Ingrese nombre del alumno: ')
        correo = _pedir_texto('Ingrese correo del alumno: ')
        telefono = _pedir_texto('Ingrese teléfono del alumno: ')
        
        mostrar_cursos()
        id_curso = _pedir_entero('Ingrese ID del curso: ')
        
        mostrar_secciones()
        id_seccion = _pedir_entero('Ingrese ID de la sección: ')
        
        # --- NUEVO CÓDIGO DE VALIDACIÓN ---
        id_apoderado = None
        while True:
            mostrar_apoderados()
            temp_id = _pedir_entero('Ingrese ID del apoderado: ')
            
            # Buscamos los datos reales del apoderado
            apoderado = obtener_objeto_apoderado(temp_id)
            
            if apoderado:
                print('\n--- VERIFICACIÓN ---')
                print(f'Vas a asociar al alumno: {nombre}')
                print(f'Con el apoderado: {apoderado.nombre}') # Muestra el nombre real
                
                confirmacion = input('¿Es correcto? (s/n): ').strip().lower()
                
                if confirmacion == 's':
                    id_apoderado = temp_id
                    break # Todo está bien, salimos del ciclo
                else:
                    print('\nVamos a pedir el ID del apoderado otra vez...\n')
            else:
                print('\nError: No existe un apoderado con ese ID. Intenta de nuevo.\n')
        # -----------------------------------

        crear_objeto_alumno(nombre, correo, telefono, id_seccion, id_curso, id_apoderado)
        
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_alumno():
    try:
        mostrar_alumnos()
        id_alumno = _pedir_entero('Ingrese el ID del alumno a modificar: ')
        encontrado = obtener_objeto_alumno(id_alumno)
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
        encontrado = obtener_objeto_alumno(id_alumno)
        if encontrado:
            eliminar_objeto_alumno(encontrado)
            print('\n¡Alumno eliminado correctamente!')
        else:
            print('Alumno no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def cambiar_curso_alumno():
    try:
        mostrar_alumnos()
        id_alumno = _pedir_entero('Ingrese el ID del alumno: ')
        alumno = obtener_objeto_alumno(id_alumno)
        mostrar_cursos()
        id_curso = _pedir_entero('Ingrese el ID del nuevo curso a asignar: ')
        curso = obtener_objeto_curso(id_curso)
        if alumno and curso:
            asignar_curso_alumno(alumno, curso)
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
        disponible = disponibilidad_sala(sala)
        print(f"¿La sala '{sala}' está disponible?: {'Sí' if disponible else 'No (Ya tiene clases programadas)'}\n")


def mostrar_asistencias_y_registros():
    print("\n--- LISTADO DE ASISTENCIAS ---")
    print(lista_asistencias(PrettyTable()))
    print("\n--- LISTADO DE REGISTROS ACADÉMICOS ---")
    print(lista_registros_academicos(PrettyTable()))


def mostrar_usuarios():
    try:
        print(lista_usuarios(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def mostrar_usuarios_habilitados():
    try:
        print(lista_usuarios_habilitados(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def mostrar_usuarios_deshabilitados():
    try:
        print(lista_usuarios_inactivos(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def agregar_usuario():
    try:
        nombre = _pedir_texto('Ingrese nombre del usuario: ')
        apellido = _pedir_texto('Ingrese apellido del usuario: ')
        correo = _pedir_texto('Ingrese correo del usuario: ')
        rut = _pedir_texto('Ingrese RUT del usuario: ')
        crear_objeto_usuario(nombre, apellido, correo, rut)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_usuario():
    try:
        mostrar_usuarios()
        id_usuario = _pedir_entero('Ingrese el ID del usuario a modificar: ')
        encontrado = obtener_objeto_usuario(id_usuario)
        if encontrado:
            print(f'\nUsuario encontrado: {encontrado.nombre} {encontrado.apellido or ""}'.strip())
            nombre = input('Nuevo nombre (o ENTER para conservar): ').strip()
            apellido = input('Nuevo apellido (o ENTER para conservar): ').strip()
            correo = input('Nuevo correo (o ENTER para conservar): ').strip()
            rut = input('Nuevo RUT (o ENTER para conservar): ').strip()
            habilitado = input('Estado habilitado (1 = Sí, 0 = No, o ENTER para conservar): ').strip()
            actualizar_objeto_usuario(nombre, apellido, correo, rut, habilitado, encontrado)
        else:
            print('Usuario no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def borrar_usuario():
    try:
        mostrar_usuarios()
        id_usuario = _pedir_entero('Ingrese el ID del usuario a eliminar: ')
        encontrado = obtener_objeto_usuario(id_usuario)
        if encontrado:
            eliminar_objeto_usuario(encontrado)
        else:
            print('Usuario no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


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
