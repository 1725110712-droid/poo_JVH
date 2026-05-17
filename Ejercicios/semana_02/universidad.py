class Universidad:
    def __init__(self,logo,oferta_educativa,localidad,sistema_informatico,modalidad,servicios,ubicacion,talleres,cantidad_salones,rector):
        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self.localidad = localidad
        self.sistema_informatico = sistema_informatico
        self.modalidad = modalidad
        self.servicios = servicios
        self.ubicacion = ubicacion 
        self.talleres = talleres 
        self.cantidad_salones = cantidad_salones
        self.rector = rector
        print(f"Logotipo de la Universidad: {self.logo}")
        print(f"Oferta educativa: {self.oferta_educativa}")
        print(f"Localidad de la Universidad: {self.localidad}")
        print(f"El sistema informatico es: {self.sistema_informatico}")
        print(f"La modalidad es: {self.modalidad}")
        print(f"Los servicios que ofrece son {self.servicios}")
        print(f"La ubicacion de la universidad es: {self.ubicacion}")
        print(f"Los talleres que ofrece son: {self.talleres}")
        print(f"Tiene un total de: {self.cantidad_salones} salones")
        print(f"El rector es: {self.rector}")
    def entretener(self):
        print("El libro es entrentenido")
    def leer(self):
        print("Leer el libro")
    def educar(self):
        print("Un libro te ayuda a educar")
    def cuidar(self):
        print("Un libro se debe de cuidar")
    def imaginar(self):
        print("Un libro te ayuda a imaginar")
unideh = Universidad ("logo.jpg","Ing.software,Turismo Alternativo,etc.","San Miguel","Cadu","Virtual","Biblioteca digital","Santa Catarina",None,None,"Octavio Castillo")

unideh.entretener()
unideh.leer()
unideh.educar()
unideh.cuidar()
unideh.imaginar()



