from datos.modelos.asignatura import Asignatura
from datos.modelos.profesor import Profesor


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


def actualizar_asignatura(asignatura: Asignatura) -> bool:
    return guardar_asignatura(asignatura)


def eliminar_asignatura(asignatura: Asignatura) -> bool:
    try:
        asignatura.delete_instance(recursive=True)
        print("Asignatura eliminada con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar asignatura: {e}")
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
