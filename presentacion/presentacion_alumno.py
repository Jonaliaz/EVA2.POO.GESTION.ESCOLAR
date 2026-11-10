from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio.negocio_alumno import (
    lista_alumnos,
    obtener_objeto_alumno,
    crear_objeto_alumno,
    actualizar_objeto_alumno,
    eliminar_objeto_alumno,
    asignar_curso_alumno
)
from negocio.negocio_apoderado import obtener_objeto_apoderado
from negocio.negocio_curso import obtener_objeto_curso
from presentacion.presentacion_curso import mostrar_cursos
from presentacion.presentacion_seccion import mostrar_secciones
from presentacion.presentacion_apoderado import mostrar_apoderados


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
