from datos.modelos.apoderado import Apoderado


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
