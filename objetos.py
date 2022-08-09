class Persona():
    """Esta clase crea la estructura para generar objetos de tipo Persona
    """
    
    def __init__(self,color,edad,estatura,nombre):
        self.color = color
        self.edad = edad
        self.estatura = estatura
        self.nombre = nombre
        
    def saltar(self):
        print('Estoy saltando')
        
persona = Persona('café',60,175,'Santiago')
persona2 = Persona('Blanca',20,190,'Cristiano Ronaldo')

class Drink:
    
    def __init__(self,name):
        self.__name = name
        
    def describe(self):
        return f'Soy una bebida de nombre: {self.__name}'
class Product:
    def __init__(self, cost, price):
        self.cost = cost
        self.price = price
        
    def get_gain(self):
        return self.price - self.cost
    
class Beer(Drink, Product):
    
    contador = 0
    
    def __init__(self,name, brand, alcohol, cost, price):
        Drink.__init__(self,name)
        Product.__init__(self,cost,price)
        self.__brand = brand
        self.__alcohol = alcohol
        
    def __describe(self):
        return super().describe() + f' de marcar {self.__brand} con {self.__alcohol} grados de alcohol'
    
    def describe(self):
        response = self.__describe()
        return response
    
    @staticmethod
    def saludar():
        print('Hola a todos')
        
beer1 = Beer('Lagger', 'Club Colombia', 5, 10, 20)
print(beer1.describe())



