from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.repositorios.repo_escuela import (
    listado_alumnos,
    guardar_alumno,
    listado_profesores,
    guardar_profesor,
    listado_cursos,
    guardar_curso,
    listado_secciones,
    guardar_seccion,
    listado_apoderados,
    guardar_apoderado,
    listado_asignaturas,
    guardar_asignatura,
    listado_contenidos,
    listado_evaluaciones,
    listado_notas,
    guardar_nota,
    listado_clases_programadas,
    listado_asistencias,
    listado_registros_academicos
)
from datos.modelos.escuela import (
    Apoderado,
    Curso,
    Profesor,
    Asignatura,
    Seccion,
    Alumno,
    Nota
)



def lista_alumnos(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre', 'Correo', 'Teléfono', 'Curso', 'Sección', 'Apoderado']
        for a in listado_alumnos():
            tabla.add_row([
                a.id_alumno,
                a.nombre,
                a.correo,
                a.telefono,
                a.id_curso.nombre,
                a.id_seccion.numero,
                a.id_apoderado.nombre
            ])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_objeto_alumno(nombre, correo, telefono, id_seccion, id_curso, id_apoderado):
    try:
        nuevo = Alumno()
        nuevo.nombre = nombre
        nuevo.correo = correo
        nuevo.telefono = telefono
        nuevo.id_seccion = id_seccion
        nuevo.id_curso = id_curso
        nuevo.id_apoderado = id_apoderado
        guardar_alumno(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_alumno(nombre, correo, telefono, id_seccion, id_curso, id_apoderado, alumno: Alumno):
    try:
        if nombre != '':
            alumno.nombre = nombre
        if correo != '':
            alumno.correo = correo
        if telefono != '':
            alumno.telefono = telefono
        if id_seccion != '':
            alumno.id_seccion = int(id_seccion)
        if id_curso != '':
            alumno.id_curso = int(id_curso)
        if id_apoderado != '':
            alumno.id_apoderado = int(id_apoderado)
        guardar_alumno(alumno)
    except Exception as error:
        print(f'{mensaje_error}{error}')



def lista_profesores(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre', 'Correo', 'Teléfono']
        for p in listado_profesores():
            tabla.add_row([p.id_profesor, p.nombre, p.correo, p.telefono])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_objeto_profesor(nombre, correo, telefono):
    try:
        nuevo = Profesor()
        nuevo.nombre = nombre
        nuevo.correo = correo
        nuevo.telefono = telefono
        guardar_profesor(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_profesor(nombre, correo, telefono, profesor: Profesor):
    try:
        if nombre != '':
            profesor.nombre = nombre
        if correo != '':
            profesor.correo = correo
        if telefono != '':
            profesor.telefono = telefono
        guardar_profesor(profesor)
    except Exception as error:
        print(f'{mensaje_error}{error}')



def lista_cursos(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre Curso', 'Nivel']
        for c in listado_cursos():
            tabla.add_row([c.id_curso, c.nombre, c.nivel])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_objeto_curso(nombre, nivel):
    try:
        nuevo = Curso()
        nuevo.nombre = nombre
        nuevo.nivel = nivel
        guardar_curso(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_curso(nombre, nivel, curso: Curso):
    try:
        if nombre != '':
            curso.nombre = nombre
        if nivel != '':
            curso.nivel = nivel
        guardar_curso(curso)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def lista_secciones(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Número Sección', 'Cupos', 'Curso', 'Asignatura']
        for s in listado_secciones():
            tabla.add_row([s.id_seccion, s.numero, s.cupos, s.id_curso.nombre, s.id_asignatura.nombre])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_objeto_seccion(numero, cupos, id_curso, id_asignatura):
    try:
        nueva = Seccion()
        nueva.numero = numero
        nueva.cupos = cupos
        nueva.id_curso = id_curso
        nueva.id_asignatura = id_asignatura
        guardar_seccion(nueva)
    except Exception as error:
        print(f'{mensaje_error}{error}')



def lista_apoderados(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre', 'Correo', 'Teléfono']
        for ap in listado_apoderados():
            tabla.add_row([ap.id_apoderado, ap.nombre, ap.correo, ap.telefono])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_objeto_apoderado(nombre, correo, telefono):
    try:
        nuevo = Apoderado()
        nuevo.nombre = nombre
        nuevo.correo = correo
        nuevo.telefono = telefono
        guardar_apoderado(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def lista_asignaturas(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Asignatura', 'Descripción', 'Profesor']
        for asig in listado_asignaturas():
            tabla.add_row([asig.id_asignatura, asig.nombre, asig.descripcion, asig.id_profesor.nombre])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_objeto_asignatura(nombre, descripcion, id_profesor):
    try:
        nueva = Asignatura()
        nueva.nombre = nombre
        nueva.descripcion = descripcion
        nueva.id_profesor = id_profesor
        guardar_asignatura(nueva)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def lista_contenidos(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre Contenido', 'Número Unidad']
        for cont in listado_contenidos():
            tabla.add_row([cont.id_contenido, cont.nombre, cont.numero_unidad])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def lista_evaluaciones(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Evaluación', 'Fecha', 'Descripción', 'Contenido']
        for ev in listado_evaluaciones():
            tabla.add_row([ev.id_evaluaciones, ev.nombre, ev.fecha, ev.descripcion, ev.id_contenido.nombre])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def lista_notas(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Alumno', 'Evaluación', 'Calificación', 'Fecha']
        for n in listado_notas():
            tabla.add_row([n.id_nota, n.id_alumno.nombre, n.id_evaluaciones.nombre, n.calificacion, n.fecha])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_objeto_nota(calificacion, fecha, id_alumno, id_evaluaciones):
    try:
        nueva = Nota()
        nueva.calificacion = calificacion
        nueva.fecha = fecha
        nueva.id_alumno = id_alumno
        nueva.id_evaluaciones = id_evaluaciones
        guardar_nota(nueva)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def lista_clases_programadas(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Horario', 'Fecha', 'Sala', 'Asignatura', 'Sección']
        for cp in listado_clases_programadas():
            tabla.add_row([cp.id_clases_prog, cp.horario, cp.fecha, cp.sala, cp.id_asignatura.nombre, cp.id_seccion.numero])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def lista_asistencias(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Fecha', 'Estado', 'Alumno', 'Horario Clase', 'Sala']
        for asis in listado_asistencias():
            tabla.add_row([
                asis.id_asistencia,
                asis.fecha,
                asis.estado,
                asis.id_alumno.nombre,
                asis.id_clases_prog.horario,
                asis.id_clases_prog.sala
            ])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def lista_registros_academicos(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Fecha', 'Curso', 'Contenido']
        for reg in listado_registros_academicos():
            tabla.add_row([reg.id_registro_academico, reg.fecha, reg.id_curso.nombre, reg.id_contenido.nombre])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')
