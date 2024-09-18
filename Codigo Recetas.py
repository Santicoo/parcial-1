class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

class GestorRecetas:
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        receta = Receta(nombre, ingredientes)
        self.recetas.append(receta)
        print(f"Receta '{nombre}' agregada correctamente.")

    def ver_recetas(self):
        if not self.recetas:
            print("No hay recetas guardadas.")
        else:
            print("Recetas guardadas:")
            for i, receta in enumerate(self.recetas, 1):
                print(f"{i}. {receta.nombre}")
            while True:
                opcion = input("Seleccione el número de la receta para ver los ingredientes (0 para volver): ")
                if opcion == "0":
                    return
                try:
                    opcion = int(opcion)
                    if opcion > 0 and opcion <= len(self.recetas):
                        receta_seleccionada = self.recetas[opcion - 1]
                        print(f"Ingredientes de la receta '{receta_seleccionada.nombre}': {', '.join(receta_seleccionada.ingredientes)}")
                        break
                    else:
                        print("Número de receta no válido.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def eliminar_receta(self, indice):
        try:
            receta_eliminada = self.recetas.pop(indice - 1)
            print(f"Receta '{receta_eliminada.nombre}' eliminada correctamente.")
        except IndexError:
            print("Índice de receta no válido.")

gestor = GestorRecetas()

while True:
    print("\nBienvenido al gestor de recetas")
    print("1. Agregar receta")
    print("2. Ver recetas")
    print("3. Eliminar receta")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la receta: ")
        ingredientes = input("Ingrese los ingredientes (separados por coma): ").split(",")
        gestor.agregar_receta(nombre, ingredientes)
    elif opcion == "2":
        gestor.ver_recetas()
    elif opcion == "3":
        gestor.ver_recetas()
        indice = int(input("Ingrese el número de la receta que desea eliminar: "))
        gestor.eliminar_receta(indice)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
