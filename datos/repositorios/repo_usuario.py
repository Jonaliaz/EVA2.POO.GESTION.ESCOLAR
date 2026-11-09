from datos.modelos.usuario import Usuarios


def listado_usuarios():
    try:
        return Usuarios.select().where(Usuarios.habilitado == 1)
    except Exception as e:
        print(f"Ha ocurrido un error al listar usuarios: {e}")
        return []


def obtener_usuario(id_usuario: int):
    try:
        return Usuarios.get(Usuarios.id_usuario == id_usuario)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener usuario: {e}")
        return None


def guardar_usuario(usuario: Usuarios) -> bool:
    try:
        usuario.save()
        print(f"Usuario guardado con éxito. ID: {usuario.id_usuario}")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al guardar usuario: {e}")
        return False


def actualizar_usuario(usuario: Usuarios) -> bool:
    return guardar_usuario(usuario)


def eliminar_usuario(usuario: Usuarios) -> bool:
    try:
        usuario.delete_instance(recursive=True)
        print("Usuario eliminado con éxito.")
        return True
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar usuario: {e}")
        return False
