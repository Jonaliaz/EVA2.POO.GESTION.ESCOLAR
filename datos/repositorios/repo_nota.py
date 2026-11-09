from datos.modelos.nota import Nota


def listado_notas():
    try:
        return Nota.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def obtener_nota(id_nota: int):
    try:
        return Nota.get(Nota.id_nota == id_nota)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener nota: {e}")
        return None


def guardar_nota(nota: Nota) -> bool:
    try:
        nota.save()
        print(f"Nota guardada con éxito. ID: {nota.id_nota}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar nota: {e}")
        return False


def actualizar_nota(nota: Nota) -> bool:
    return guardar_nota(nota)


def eliminar_nota(nota: Nota) -> bool:
    try:
        nota.delete_instance(recursive=True)
        print("Nota eliminada con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar nota: {e}")
        return False
