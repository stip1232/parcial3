# modelo_granja.py

from basededatos import BaseDatos

class Interfaz:
    def __init__(self):
        self.db = BaseDatos()

    def menu(self):
        while True:
            print("\n🐔=== SISTEMA DE REGISTRO DE GRANJA ===🐣")
            print("1. Agregar animal")
            print("2. Mostrar animales")
            print("3. Registrar producción semanal")
            print("4. Actualizar datos del animal")
            print("5. Eliminar animal")
            print("6. Buscar animal")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                codigo = input("Código: ")
                raza = input("Raza: ")
                edad = int(input("Edad: "))
                self.db.agregar_animal(codigo, raza, edad)

            elif opcion == "2":
                self.db.mostrar_animales()

            elif opcion == "3":
                codigo = input("Código del animal: ")
                cantidad = int(input("Cantidad de huevos producidos esta semana: "))
                animal = self.db.buscar_animal(codigo)
                if animal:
                    animal.registrar_produccion(cantidad)
                    print("✅ Producción registrada correctamente.")

            elif opcion == "4":
                codigo = input("Código del animal a actualizar: ")
                nueva_raza = input("Nueva raza (dejar vacío si no aplica): ")
                nueva_edad = input("Nueva edad (dejar vacío si no aplica): ")
                self.db.actualizar_animal(codigo, nueva_raza or None, int(nueva_edad) if nueva_edad else None)

            elif opcion == "5":
                codigo = input("Código del animal a eliminar: ")
                self.db.eliminar_animal(codigo)

            elif opcion == "6":
                codigo = input("Código del animal: ")
                animal = self.db.buscar_animal(codigo)
                if animal:
                    print(animal)

            elif opcion == "7":
                print("👋 Saliendo del sistema...")
                break

            else:
                print("⚠️ Opción no válida, intente de nuevo.")
