
# animal.py

class Animal:
    def __init__(self, codigo, raza, edad):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad
        self.huevos_semana = 0

    def registrar_produccion(self, cantidad):
        self.huevos_semana += cantidad

    def reiniciar_produccion(self):
        self.huevos_semana = 0

    def __str__(self):
        return f"Código: {self.codigo}, Raza: {self.raza}, Edad: {self.edad} años, Huevos/Semana: {self.huevos_semana}"
