from presentación.menu import menu_principal
from datos.repositorios.repo_escuela import listado_cursos

# Ejecutamos la función para obtener la lista de cursos
cursos = listado_cursos()

# Recorremos e imprimimos los cursos
for curso in cursos:
    print(curso)

# Si deseas llamar al menú principal, descomenta la siguiente línea:
# menu_principal()