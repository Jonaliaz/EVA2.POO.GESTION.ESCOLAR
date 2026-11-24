from prettytable import PrettyTable
from auxiliares import (
    mensaje_error,
    validar_largo_string,
    validar_correo,
    validar_numero
)
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


def _pedir_correo(mensaje: str, largo: int = 50, opcional: bool = False) -> str:
    while True:
        entrada = input(mensaje).strip()
        if entrada == '':
            if opcional:
                return ''
            print("El campo no puede estar vacío.")
            continue
        if largo > 0:
            val_largo, msg_largo = validar_largo_string(entrada, largo)
            if val_largo == '':
                print(msg_largo)
                continue
        correo, msg = validar_correo(entrada)
        print(msg)
        if correo != '':
            return correo


def _pedir_telefono(mensaje: str, largo: int = 50, opcional: bool = False) -> str:
    while True:
        entrada = input(mensaje).strip()
        if entrada == '':
            if opcional:
                return ''
            print("El campo no puede estar vacío.")
            continue
        if largo > 0:
            val_largo, msg_largo = validar_largo_string(entrada, largo)
            if val_largo == '':
                print(msg_largo)
                continue
        numero, msg = validar_numero(entrada)
        print(msg)
        if numero != 0 or entrada == '0':
            return str(numero)


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


def _pedir_entero_opcional(mensaje: str) -> str:
    while True:
        entrada = input(mensaje).strip()
        if entrada == '':
            return ''
        numero, msg = validar_numero(entrada)
        if numero == 0 and entrada != '0':
            print(msg)
        else:
            return str(numero)


def mostrar_alumnos():
    try:
        print(lista_alumnos(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


#confirmacion para los id de los usuarios
def agregar_alumno():
    try:
        nombre = _pedir_texto('Ingrese nombre del alumno: ', 60)
        correo = _pedir_correo('Ingrese correo del alumno: ', 50)
        telefono = _pedir_telefono('Ingrese teléfono del alumno: ', 50)
        
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
            nombre = _pedir_texto_opcional('Nuevo nombre (o ENTER para conservar): ', 60)
            correo = _pedir_correo('Nuevo correo (o ENTER para conservar): ', 50, opcional=True)
            telefono = _pedir_telefono('Nuevo teléfono (o ENTER para conservar): ', 50, opcional=True)
            id_seccion = _pedir_entero_opcional('Nuevo ID sección (o ENTER para conservar): ')
            id_curso = _pedir_entero_opcional('Nuevo ID curso (o ENTER para conservar): ')
            id_apoderado = _pedir_entero_opcional('Nuevo ID apoderado (o ENTER para conservar): ')
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
