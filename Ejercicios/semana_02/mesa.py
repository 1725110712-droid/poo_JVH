class Mesa:
    def __init__(self,color,altura,patas,ensamble,textura,ancho,material,dureza,largo,forma):
        self.color = color 
        self.altura = altura
        self.patas = patas
        self.ensamble = ensamble 
        self.textura = textura
        self.ancho = ancho
        self.material = material
        self.dureza = dureza
        self.largo = largo
        self.forma = forma
        print(f"El color de la mesa es: {self.color}")
        print(f"la altura de la mesa es de: {self.altura}")
        print(f"la cantidad de patas es: {self.patas} patas")
        print(f"el esanmble que tiene es: {self.ensamble}")
        print(f"la textura que tiene es: {self.textura}")
        print(f"el ancho de la mesa es de: {self.ancho}")
        print(f"el material del que est hecha la mesa es de: {self.material}")
        print(f"la dureza de la mesa es de: {self.dureza}")
        print(f"el largo de la mesa es de: {self.largo}")
        print(f"la forma de la mesa es: {self.forma}")
    def sostener(self):
        print ("La mesa puede sostener objetos")
    def mover(self):
        print ("La mesa puede moverse")
    def limpiar(self):
        print("La mesa puede limpiarse con un trapo")
    def nivelar(self):
        print("se puede colocar un papel en una de las patas cuando el terreno es irregular")
    def cubrir(self):
        print("la mesa se puede cubrir con un mantel para cambiar su aspec to fisico")
mesa_comun = Mesa ("Marron","75cm","4 patas","union fija","lisa","100 cm","madera barnizada","Alta","120 cm","Rectangular")

mesa_comun.sostener() 
mesa_comun.mover()
mesa_comun.limpiar()
mesa_comun.nivelar()
mesa_comun.cubrir() 
