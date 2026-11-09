from datos.modelos.alumno import Alumno
from datos.modelos.curso import Curso


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
