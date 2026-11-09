from datos.modelos.contenido import Contenido


def listado_contenidos():
    try:
        return Contenido.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def obtener_contenido(id_contenido: int):
    try:
        return Contenido.get(Contenido.id_contenido == id_contenido)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener contenido: {e}")
        return None


def guardar_contenido(contenido: Contenido) -> bool:
    try:
        contenido.save()
        print(f"Contenido guardado con éxito. ID: {contenido.id_contenido}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar contenido: {e}")
        return False


def actualizar_contenido(contenido: Contenido) -> bool:
    return guardar_contenido(contenido)


def eliminar_contenido(contenido: Contenido) -> bool:
    try:
        contenido.delete_instance(recursive=True)
        print("Contenido eliminado con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar contenido: {e}")
        return False
