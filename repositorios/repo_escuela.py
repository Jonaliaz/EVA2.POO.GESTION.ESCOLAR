from modelos.escuela import Escuela  # Importas la clase modelo creada en modelos/escuela.py

def listado_cursos():
    # Obtiene todos los registros usando Peewee ORM
    cursos = Escuela.select()
    return cursos