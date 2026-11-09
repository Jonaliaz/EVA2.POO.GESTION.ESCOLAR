from datos.modelos.profesor import Profesor
from datos.modelos.asignatura import Asignatura


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
