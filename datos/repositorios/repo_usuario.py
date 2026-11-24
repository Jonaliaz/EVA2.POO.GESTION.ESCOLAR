from datos.modelos.usuario import Usuarios


def listado_usuarios():
    try:
        return Usuarios.select()
    except Exception as e:
        print(f"Ha ocurrido un error al listar usuarios: {e}")
        return []


def listado_usuarios_habil():
    try:
        return Usuarios.select().where(Usuarios.habilitado == 1)
    except Exception as e:
        print(f"Ha ocurrido un error al listar usuarios habilitados: {e}")
        return []


def listado_usuarios_deshabilitados():
    try:
        return Usuarios.select().where(Usuarios.habilitado == 0)
    except Exception as e:
        print(f"Ha ocurrido un error al listar usuarios: {e}")
        return []


def obtener_usuario(id_usuario: int):
    try:
        return Usuarios.get(Usuarios.id_usuario == id_usuario)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener usuario: {e}")
        return None


def obtener_usuario_correo(correo: str):
    try:
        return Usuarios.get_or_none(Usuarios.correo == correo)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener usuario por correo: {e}")
        return None


def obtener_usuario_rut(rut: str):
    try:
        return Usuarios.get_or_none(Usuarios.rut == rut)
    except Exception as e:
        print(f"Ha ocurrido un error al obtener usuario por RUT: {e}")
        return None


def obtener_usuario_correo_o_rut(identificador: str):
    try:
        return Usuarios.get_or_none(
            (Usuarios.correo == identificador) | (Usuarios.rut == identificador)
        )
    except Exception as e:
        print(f"Ha ocurrido un error al buscar usuario por correo o RUT: {e}")
        return None


buscar_usuario_por_correo = obtener_usuario_correo
buscar_usuario_por_rut = obtener_usuario_rut
buscar_usuario_login = obtener_usuario_correo_o_rut


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
