class Perro:
    def __init__(self,raza,edad,nombre,peso,color,animo,energia,vacunas,collar,tamaño):
        self.raza = raza
        self.edad = edad
        self.nombre = nombre
        self.peso = peso
        self.color = color
        self.animo = animo 
        self.energia = energia
        self.vacunas = vacunas
        self.collar = collar
        self.tamaño = tamaño
        print(f"la raza del perro es: {self.raza}")
        print(f"la edad del perro es: {self.edad}")
        print(f"el nombre del perro es: {self.nombre}")
        print(f"el peso del perro es: {self.peso}")
        print(f"el color del perro es: {self.color}")
        print(f"el animo del perro actualmente es: {self.animo}")
        print(f"la energia que el perro tiene es: {self.energia}")
        print(f"el perro tiene todas sus vacunas {self.vacunas}")
        print(f"el perro cuenta con collar: {self.collar}")
        print(f"el tamaño del perro es: {self.tamaño}")
    def ladrar(self):
        print("el perro puede ladrar")
    def comer(self):
        print("el perro puede comer")
    def mover(self):
        print("el perro puede mover la cola cuando esta feliz")
    def dormir(self):
        print("el perro puede irse a dormir cuando se canse")
    def traer(self):
        print("el perro puede traer la pelota a modo de juego")
pitbull = Perro ("Pitbull","3 años","Princesa","15kg","negro","Feliz","Muy alta","Tiene todas","cuenta con collar de color rojo","Grande")

pitbull.ladrar()
pitbull.comer()
pitbull.mover()
pitbull.dormir()
pitbull.traer()