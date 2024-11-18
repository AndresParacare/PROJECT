class Persona:
    def __init__(self, nombre, edad, domicilio, telefono, correo_electronico, estatura, peso, color_de_ojos):
        self.nombre = nombre
        self.edad = edad
        self.domicilio = domicilio
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.estatura = estatura
        self.peso = peso
        self.color_de_ojos = color_de_ojos
        self.nacionalidad = None 

    def presentar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Domicilio: {self.domicilio}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo Electrónico: {self.correo_electronico}")
        print(f"Estatura: {self.estatura} m")
        print(f"Peso: {self.peso} kg")
        print(f"Color de Ojos: {self.color_de_ojos}")
        print(f"Nacionalidad: {self.nacionalidad}")

    def calcularEdad(self, anio_actual):
        return anio_actual - self.edad
    
    def compararEstatura(self, otra_persona):
        return self.estatura > otra_persona.estatura

    def calcularIMC(self):
        return self.peso / (self.estatura ** 2)
    
    def mostrarNacionalidad(self):
        return self.nacionalidad

persona = Persona("Eduardo", 28, "Cota 905", 58412123456, "edu.koki@gmail.com", 1.80, 70, "Verde")
persona2 = Persona("Carlos", 25, "Calle A 1", 123456789, "carlos@example.com", 1.70, 75, "Marrón")
persona.nacionalidad = "Colombiana"
persona.presentar_informacion()
edad_actual = persona.calcularEdad(2024)
print(f"{persona.nombre} nacio en {edad_actual} y tiene {persona.edad}")
if persona.compararEstatura(persona2):
    print(f"{persona.nombre} es más alto que {persona2.nombre}.")
else:
    print(f"{persona2.nombre} es más bajo que {persona.nombre}.")
imc = persona.calcularIMC()
print(f"El peso ideal de {persona.nombre} es de: {imc:.2f}")
nacionalidad = persona.mostrarNacionalidad()
print(f"La nacionalidad es {nacionalidad}")