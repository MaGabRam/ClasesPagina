# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

# Definición de la clase Estudiante que hereda de Persona


class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.matricula = matricula

    def mostrar_informacion(self):
        super().mostrar_informacion()  # Llama al método de la clase base
        print(f'Matrícula: {self.matricula}')


# Crear una instancia de Persona
persona1 = Persona('Ana', 30)
persona1.mostrar_informacion()

# Crear una instancia de Estudiante
estudiante1 = Estudiante('Luis', 20, 'A12345')
estudiante1.mostrar_informacion()
