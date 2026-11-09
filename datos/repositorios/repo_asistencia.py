from datos.modelos.asistencia import Asistencia


def listado_asistencias():
    try:
        return Asistencia.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def obtener_asistencia(id_asistencia: int):
    try:
        return Asistencia.get(Asistencia.id_asistencia == id_asistencia)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener asistencia: {e}")
        return None


def guardar_asistencia(asistencia: Asistencia) -> bool:
    try:
        asistencia.save()
        print(f"Asistencia guardada con éxito. ID: {asistencia.id_asistencia}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar asistencia: {e}")
        return False


def actualizar_asistencia(asistencia: Asistencia) -> bool:
    return guardar_asistencia(asistencia)


def eliminar_asistencia(asistencia: Asistencia) -> bool:
    try:
        asistencia.delete_instance(recursive=True)
        print("Asistencia eliminada con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar asistencia: {e}")
        return False
