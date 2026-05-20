class PersonajeJuego:
    def __init__ (self,estatura,complexion,postura_corporal,color_piel,cabello,modificaciones,color_ojos,tatuajes,humano,poderes):
        self.estatura = estatura
        self.complexion = complexion
        self.postura_corporal = postura_corporal
        self.color_piel = color_piel
        self.cabello = cabello 
        self.modificaciones = modificaciones
        self.color_ojos = color_ojos
        self.tatuajes = tatuajes
        self.humano = humano 
        self.poderes = poderes
        print(f"la estatura del personaje es: {self.estatura}")
        print(f"la complexion del personaje es: {self.complexion}")
        print(f"la postura corporal del personaje es: {self.postura_corporal}")
        print(f"el color de piel del personaje es: {self.color_piel}")
        print(f"el cabello del personaje es: {self.cabello}")
        print(f"el personaje tiene modificaciones: {self.modificaciones}")
        print(f"el color de ojos del personaje es: {self.color_ojos}")
        print(f"el personaje tiene tatuajes: {self.tatuajes}")
        print(f"el personaje es humano: {self.humano}")
        print(f"el persoanje tiene poderes: {self.poderes}")
    def mover(self):
        print("el personaje se puede mover")
    def correr(self):
        print("el personaje puede correr por un tiempo limitado")
    def rodar(self):
        print("el personaje puede rodar para moverse mas rapido")
    def esquivar(self):
        print("el personaje haciendo una accion concreta puede esquivar")
    def bloquear(self):
        print("el personaje puede bloquear y devolver ciertos ataques")
link = PersonajeJuego ("1.60","Atletico y delgado","erguida,alerta y heroica","piel clara","rubio y semilargo","brazo derecho reemplazado con un brazo mistico","azul brillante","no tiene","no es humano","tiene manipulacion de objetos y capacidad de fusion de objetos")

link.mover()
link.correr()
link.rodar()
link.esquivar()
link.bloquear()