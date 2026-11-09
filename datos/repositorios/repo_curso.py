from datos.modelos.curso import Curso


def listado_cursos():
    try:
        return Curso.select()
    except Exception as e:
        print(f"Ha ocurrido un error al listar cursos: {e}")
        return []


def obtener_curso(id_curso: int):
    try:
        return Curso.get(Curso.id_curso == id_curso)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener curso: {e}")
        return None


def guardar_curso(curso: Curso) -> bool:
    try:
        curso.save()
        print(f"Curso guardado con éxito. ID: {curso.id_curso}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar curso: {e}")
        return False


def actualizar_curso(curso: Curso) -> bool:
    return guardar_curso(curso)


def eliminar_curso(curso: Curso) -> bool:
    try:
        curso.delete_instance(recursive=True)
        print("Curso eliminado con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar curso: {e}")
        return False
