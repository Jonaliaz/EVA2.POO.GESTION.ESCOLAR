import sys
from auxiliares.opcioens_menu import menu_superior
print ()
def menu_principal():
    print("Gestión Escolar")
    print("----------------")
while True:
    for clave, valor in menu_superior.items():
        print(f"[{clave}] {valor}")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("seleccionaste Gestión de Alumnos\n")
    elif opcion == "2":
        print("seleccionaste Gestión de Profesores\n")
    elif opcion == "3":
        print("Saliendo del programa...")
        sys.exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu_principal()