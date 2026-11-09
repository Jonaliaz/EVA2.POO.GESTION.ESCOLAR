from datos.modelos.clases_programadas import Clases_programadas


def listado_clases_programadas():
    try:
        return Clases_programadas.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def obtener_clase_programada(id_clases_prog: int):
    try:
        return Clases_programadas.get(Clases_programadas.id_clases_prog == id_clases_prog)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener clase programada: {e}")
        return None


def guardar_clase_programada(clase_prog: Clases_programadas) -> bool:
    try:
        clase_prog.save()
        print(f"Clase programada guardada con éxito. ID: {clase_prog.id_clases_prog}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar clase programada: {e}")
        return False


def actualizar_clase_programada(clase_prog: Clases_programadas) -> bool:
    return guardar_clase_programada(clase_prog)


def eliminar_clase_programada(clase_prog: Clases_programadas) -> bool:
    try:
        clase_prog.delete_instance(recursive=True)
        print("Clase programada eliminada con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar clase programada: {e}")
        return False


def verificar_disponibilidad_de_sala(sala: str) -> bool:
    try:
        ocupada = Clases_programadas.select().where(Clases_programadas.sala == sala).exists()
        return not ocupada
    except Exception as e:
        print(f"Ha ocurrido un error al verificar sala: {e}")
        return False
