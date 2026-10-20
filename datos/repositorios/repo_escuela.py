from datos.modelos.escuela import (
    Apoderado,
    Curso,
    Profesor,
    Asignatura,
    Contenido,
    Evaluaciones,
    Seccion,
    Alumno,
    Registro_academico,
    Clases_programadas,
    Nota,
    Asistencia
)

def listado_apoderados():
    try:
        return Apoderado.select()
    except Exception as e:
        print(f"Ha ocurrido un error al listar apoderados: {e}")
        return []
    
    
def obtener_apoderado(id_apoderado: int):
    try:
        return Apoderado.get(Apoderado.id_apoderado == id_apoderado)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener apoderado: {e}")
        return None


def guardar_apoderado(apoderado: Apoderado) -> bool:
    try:
        apoderado.save()
        print(f"Apoderado guardado con éxito. ID: {apoderado.id_apoderado}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar apoderado: {e}")
        return False


def actualizar_apoderado(apoderado: Apoderado) -> bool:
    return guardar_apoderado(apoderado)


def eliminar_apoderado(apoderado: Apoderado) -> bool:
    try:
        apoderado.delete_instance(recursive=True)
        print("Apoderado eliminado con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar apoderado: {e}")
        return False
    
    
def listado_cursos():
    try:
        return Curso.select()
    except Exception as e:
        print(f"Ha ocurrido un error al listar cursos: {e}")
        return []


def obtener_curso(id_curso: int):
    try:
        return Curso.get(Curso.id_curso == id_curso)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener curso: {e}")
        return None


def guardar_curso(curso: Curso) -> bool:
    try:
        curso.save()
        print(f"Curso guardado con éxito. ID: {curso.id_curso}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar curso: {e}")
        return False


def actualizar_curso(curso: Curso) -> bool:
    return guardar_curso(curso)


def eliminar_curso(curso: Curso) -> bool:
    try:
        curso.delete_instance(recursive=True)
        print("Curso eliminado con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar curso: {e}")
        return False
    


def listado_profesores():
    try:
        return Profesor.select()
    except Exception as e:
        print(f"Ha ocurrido un error al listar profesores: {e}")
        return []


def obtener_profesor(id_profesor: int):
    try:
        return Profesor.get(Profesor.id_profesor == id_profesor)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener profesor: {e}")
        return None


def guardar_profesor(profesor: Profesor) -> bool:
    try:
        profesor.save()
        print(f"Profesor guardado con éxito. ID: {profesor.id_profesor}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar profesor: {e}")
        return False


def actualizar_profesor(profesor: Profesor) -> bool:
    return guardar_profesor(profesor)


def eliminar_profesor(profesor: Profesor) -> bool:
    try:
        profesor.delete_instance(recursive=True)
        print("Profesor eliminado con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar profesor: {e}")
        return False


def asignar_asignatura(profesor: Profesor, asignatura: Asignatura) -> bool:
    try:
        asignatura.id_profesor = profesor.id_profesor
        asignatura.save()
        print(f"Asignatura '{asignatura.nombre}' asignada al profesor '{profesor.nombre}'.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al asignar asignatura: {e}")
        return False
    

def listado_alumnos():
    try:
        return Alumno.select()
    except Exception as e:
        print(f"Ha ocurrido un error al listar alumnos: {e}")
        return []


def obtener_alumno(id_alumno: int):
    try:
        return Alumno.get(Alumno.id_alumno == id_alumno)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener alumno: {e}")
        return None


def guardar_alumno(alumno: Alumno) -> bool:
    try:
        alumno.save()
        print(f"Alumno guardado con éxito. ID: {alumno.id_alumno}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar alumno: {e}")
        return False


def actualizar_alumno(alumno: Alumno) -> bool:
    return guardar_alumno(alumno)


def eliminar_alumno(alumno: Alumno) -> bool:
    try:
        alumno.delete_instance(recursive=True)
        print("Alumno eliminado con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar alumno: {e}")
        return False


def asignar_curso(alumno: Alumno, curso: Curso) -> bool:
    try:
        alumno.id_curso = curso.id_curso
        alumno.save()
        print(f"Curso '{curso.nombre}' asignado al alumno '{alumno.nombre}'.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al asignar curso: {e}")
        return False
    

def listado_asignaturas():
    try:
        return Asignatura.select()
    except Exception as e:
        print(f"Ha ocurrido un error al listar asignaturas: {e}")
        return []


def obtener_asignatura(id_asignatura: int):
    try:
        return Asignatura.get(Asignatura.id_asignatura == id_asignatura)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener asignatura: {e}")
        return None


def guardar_asignatura(asignatura: Asignatura) -> bool:
    try:
        asignatura.save()
        print(f"Asignatura guardada con éxito. ID: {asignatura.id_asignatura}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar asignatura: {e}")
        return False
    
    
def listado_secciones():
    try:
        return Seccion.select()
    except Exception as e:
        print(f"Ha ocurrido un error al listar secciones: {e}")
        return []


def guardar_seccion(seccion: Seccion) -> bool:
    try:
        seccion.save()
        print(f"Sección guardada con éxito. ID: {seccion.id_seccion}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar sección: {e}")
        return False
    
    
def listado_contenidos():
    try:
        return Contenido.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def listado_evaluaciones():
    try:
        return Evaluaciones.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def listado_notas():
    try:
        return Nota.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def guardar_nota(nota: Nota) -> bool:
    try:
        nota.save()
        print(f"Nota guardada con éxito. ID: {nota.id_nota}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar nota: {e}")
        return False


def listado_clases_programadas():
    try:
        return Clases_programadas.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def verificar_disponibilidad_de_sala(sala: str) -> bool:
    try:
        ocupada = Clases_programadas.select().where(Clases_programadas.sala == sala).exists()
        return not ocupada
    except Exception as e:
        print(f"Ha ocurrido un error al verificar sala: {e}")
        return False


def listado_asistencias():
    try:
        return Asistencia.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def listado_registros_academicos():
    try:
        return Registro_academico.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []
    
    