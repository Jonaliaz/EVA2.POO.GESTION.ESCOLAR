from datos.modelos.seccion import Seccion


def listado_secciones():
    try:
        return Seccion.select()
    except Exception as e:
        print(f"Ha ocurrido un error al listar secciones: {e}")
        return []


def obtener_seccion(id_seccion: int):
    try:
        return Seccion.get(Seccion.id_seccion == id_seccion)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener sección: {e}")
        return None


def guardar_seccion(seccion: Seccion) -> bool:
    try:
        seccion.save()
        print(f"Sección guardada con éxito. ID: {seccion.id_seccion}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar sección: {e}")
        return False


def actualizar_seccion(seccion: Seccion) -> bool:
    return guardar_seccion(seccion)


def eliminar_seccion(seccion: Seccion) -> bool:
    try:
        seccion.delete_instance(recursive=True)
        print("Sección eliminada con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar sección: {e}")
        return False
