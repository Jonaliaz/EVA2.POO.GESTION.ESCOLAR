from datos.modelos.registro_academico import Registro_academico


def listado_registros_academicos():
    try:
        return Registro_academico.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def obtener_registro_academico(id_registro_academico: int):
    try:
        return Registro_academico.get(Registro_academico.id_registro_academico == id_registro_academico)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener registro académico: {e}")
        return None


def guardar_registro_academico(registro: Registro_academico) -> bool:
    try:
        registro.save()
        print(f"Registro académico guardado con éxito. ID: {registro.id_registro_academico}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar registro académico: {e}")
        return False


def actualizar_registro_academico(registro: Registro_academico) -> bool:
    return guardar_registro_academico(registro)


def eliminar_registro_academico(registro: Registro_academico) -> bool:
    try:
        registro.delete_instance(recursive=True)
        print("Registro académico eliminado con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar registro académico: {e}")
        return False
