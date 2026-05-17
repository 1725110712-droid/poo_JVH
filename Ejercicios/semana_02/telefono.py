class Smartphone:
    def __init__(self,marca,procesador,pantalla,camara,almacenamiento,memoria_ram,precio,bateria,carga,sistema_operativo):
        self.marca = marca
        self.procesador = procesador 
        self.pantalla = pantalla 
        self.camara = camara
        self.almacenamiento = almacenamiento
        self.memoria_ram = memoria_ram
        self.precio = precio 
        self.bateria = bateria
        self.carga = carga
        self.sistema_operativo = sistema_operativo
        print(f"La marca del telefono es: {self.marca}")
        print(f"El procesador que viene equipado es: {self.procesador}")
        print(f"La pantalla del telefono es: {self.pantalla}")
        print(f"La camara del telefono es: {self.camara}")
        print(f"El almacenamiento que tiene es: {self.almacenamiento}")
        print(f"La memoria RAM que tiene es: {self.memoria_ram}")
        print(f"El precio del telefono ronda en: {self.precio}")
        print(f"La bateria que tiene el telefono es de: {self.bateria}")
        print(f"La  carga que soporta el telefono es: {self.carga}")
        print(f"El sistema operativo que maneja es: {self.sistema_operativo}")
    def llamar(self):
        print("Con el telefono puedes llamar")
    def entrenener(self):
        print("El telefono tiene muchas app de entretenimiento")
    def conocer(self):
        print("El telefono puede ayudate a conocer muchas cosas")
    def guardar(self):
        print("En el telefono puede guardar mucha de tu informacion")
    def comprar(self):
        print("Con el telefono puedes pedir cosas a domicilio")
oppo_a57 = Smartphone ("Oppo","MediaTek Helio G35","LCD IPS de 6.56 pulgadas","Trasera de 13MP + 2MP y frontal de 8MP","128 GB","4GB","$2600 a $3500","5000 mAh","SUPERVOOC de 33W","Android 12")

oppo_a57.llamar()
oppo_a57.entrenener()
oppo_a57.conocer()
oppo_a57.guardar()
oppo_a57.comprar()
