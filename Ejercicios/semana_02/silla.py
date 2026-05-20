class Silla:
    def __init__ (self,material,color,num_patas,tipo_respaldo,capacidad,altura,comfort,movilidad,estado,ancho):
        self.material = material 
        self.color = color 
        self.num_patas = num_patas
        self.tipo_respaldo = tipo_respaldo
        self.capacidad = capacidad 
        self.altura = altura 
        self.comfort = comfort
        self.movilidad = movilidad
        self.estado = estado
        self.ancho = ancho
        print(f"el material del que esta hecha es:{self.material}")
        print(f"el color de la silla es:{self.color}")
        print(f"la cantidad de patas que tiene la silla es de: {self.num_patas} patas")
        print(f"el tipo de respaldo que tiene es: {self.tipo_respaldo}")
        print(f"la capacidad de la silla es de: {self.capacidad}")
        print(f"la altura de la silla es de: {self.altura}")
        print(f"el tipo de confort que tiene la silla es de: {self.comfort}")
        print(f"la movilidad de la silla es por medio de: {self.movilidad}")
        print(f"el estado de la silla es de: {self.estado}")
        print(f"el ancho de la siila es de: {self.ancho}")
    def regular(self):
        print("La silla puede regular su altura")
    def rotar(self):
        print("la silla puede rotar sobre su eje ")
    def dezplazar(self):
        print("la silla se puede mover empujandola")
    def bloquear(self):
        print("la silla puede bloquear el respaldo al empujar la palanca")
    def ajustar(self):
        print("La silla tiene una pieza en especifico para ajustar el apoyo lumbar")
silla_oficina = Silla ("Plastico","Negro","5 patas","Tipo malla","120 kg","40 cm","cojin acolchado","Ruedas","Libre","60 cm")

silla_oficina.regular()
silla_oficina.rotar ()
silla_oficina.dezplazar()
silla_oficina.bloquear ()
silla_oficina.ajustar ()


