class Persona():
    
    def __init__(self,color,edad,estatura,nombre):
        self.color = color
        self.edad = edad
        self.estatura = estatura
        self.nombre = nombre
        
    def saltar(self):
        print('Estoy saltando')
        
persona = Persona('café',60,175,'Santiago')
persona2 = Persona('Blanca',20,190,'Cristiano Ronaldo')
print(persona2.nombre)


        