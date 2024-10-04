class Persona:
    def __init__(self, nombre, edad, altura, peso, ocupacion):
        # Atributos de la clase Persona
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.ocupacion = ocupacion

    # Método 1: Saludar
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

    # Método 2: Mostrar ocupación
    def mostrar_ocupacion(self):
        print(f"Mi ocupación es {self.ocupacion}.")

    # Método 3: Actualizar peso
    def actualizar_peso(self, nuevo_peso):
        self.peso = nuevo_peso
        print(f"Mi nuevo peso es {self.peso} kg.")

    # Método 4: Mostrar información personal
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Altura: {self.altura} m, Peso: {self.peso} kg, Ocupación: {self.ocupacion}.")

    # Método 5: Celebrar cumpleaños
    def celebrar_cumpleanos(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años.")

    # Método 6: Saludar
    def mandar_saludo(self, otraPersona):
        print(f"¡{self.nombre}! Te manda saludos {otraPersona}. ")


# Crear una instancia de la clase Persona
persona1 = Persona("Carlos", 28, 1.75, 70, "Ingeniero")
persona2 = Persona("Rose", 19, 1.75, 70, "Cantante")
persona3 = Persona("Yone", 32, 1.75, 70, "Campeon")


# Llamar a los métodos de la instancia
persona1.saludar()                 # Método 1
persona1.mostrar_ocupacion()        # Método 2
persona1.actualizar_peso(72)        # Método 3
persona1.mostrar_info()           # Método 4
persona1.celebrar_cumpleanos(  )      # Método 5
persona2.saludar()                 # Método 1
persona2.mostrar_ocupacion()        # Método 2
persona2.actualizar_peso(72)        # Método 3
persona2.mostrar_info()           # Método 4
persona2.celebrar_cumpleanos(  )      # Método 5
persona3.saludar()                 # Método 1
persona3.mostrar_ocupacion()        # Método 2
persona3.actualizar_peso(72)        # Método 3
persona3.mostrar_info()           # Método 4
persona3.celebrar_cumpleanos(  )      # Método 5
persona3.mandar_saludo(persona2.nombre)            #Método 6
