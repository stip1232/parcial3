# basedatos.py

from animal import Animal

class BaseDatos:
    def __init__(self):
        self.animales = []

    # CREATE
    def agregar_animal(self, codigo, raza, edad):
        if any(a.codigo == codigo for a in self.animales):
            print("⚠️ Ya existe un animal con ese código.")
        else:
            self.animales.append(Animal(codigo, raza, edad))
            print("✅ Animal agregado correctamente.")

    # READ
    def mostrar_animales(self):
        if not self.animales:
            print("📭 No hay animales registrados.")
        else:
            for a in self.animales:
                print(a)

    def buscar_animal(self, codigo):
        for a in self.animales:
            if a.codigo == codigo:
                return a
        print("❌ Animal no encontrado.")
        return None

    # UPDATE
    def actualizar_animal(self, codigo, nueva_raza=None, nueva_edad=None):
        animal = self.buscar_animal(codigo)
        if animal:
            if nueva_raza:
                animal.raza = nueva_raza
            if nueva_edad:
                animal.edad = nueva_edad
            print("✅ Datos del animal actualizados correctamente.")

    # DELETE
    def eliminar_animal(self, codigo):
        animal = self.buscar_animal(codigo)
        if animal:
            self.animales.remove(animal)
            print("🗑️ Animal eliminado correctamente.")
