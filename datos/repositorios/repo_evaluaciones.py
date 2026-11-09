from datos.modelos.evaluaciones import Evaluaciones


def listado_evaluaciones():
    try:
        return Evaluaciones.select()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return []


def obtener_evaluacion(id_evaluaciones: int):
    try:
        return Evaluaciones.get(Evaluaciones.id_evaluaciones == id_evaluaciones)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener evaluación: {e}")
        return None


def guardar_evaluacion(evaluacion: Evaluaciones) -> bool:
    try:
        evaluacion.save()
        print(f"Evaluación guardada con éxito. ID: {evaluacion.id_evaluaciones}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar evaluación: {e}")
        return False


def actualizar_evaluacion(evaluacion: Evaluaciones) -> bool:
    return guardar_evaluacion(evaluacion)


def eliminar_evaluacion(evaluacion: Evaluaciones) -> bool:
    try:
        evaluacion.delete_instance(recursive=True)
        print("Evaluación eliminada con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar evaluación: {e}")
        return False
