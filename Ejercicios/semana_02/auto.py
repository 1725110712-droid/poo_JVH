class auto:
    def __init__(self,marca,modelo,anio_fabricacion,color,tipo_motor,transmision,numero_puertas,kilometraje,peso,capacidad_pasajeros):
        self.marca = marca 
        self.modelo = modelo
        self.anio_fabricacion = anio_fabricacion
        self.color = color 
        self.tipo_motor = tipo_motor
        self.transmision = transmision 
        self.numero_puertas = numero_puertas 
        self.kilometraje = kilometraje
        self.peso = peso
        self.capacidad_pasajeros = capacidad_pasajeros
        print(f"La marca del auto es: {self.marca}")
        print(f"La fabricacion del auto fue en el año: {self.anio_fabricacion}")
        print(f"El color del auto es: {self.color}")
        print(f"El tipo de motor del auto: {self.tipo_motor}")
        print(f"La transmision que tiene el auto es: {self.transmision}")
        print(f"El numero de puertas que tiene el auto es de: {self.numero_puertas}")
        print(f"El kilometraje que tiene el auto es de: {self.kilometraje}")
        print(f"El peso del vehiculo es de: {self.peso}")
        print(f"La cantidad de personas que puede llevar el auto es de: {self.capacidad_pasajeros}")
    def viajar(self):
        print("El auto puede llevarte a donde sea")
    def avanzar(self):
        print("El auto puede avanzar a donde se le indique mediante el volante y las velocidades")
    def encender(self):
        print("Podemos encender el auto con un simple movimiento ya sea una llave o un boton")
    def frenar(self):
        print("El auto puede detenerse en cualquier momento por intromision del conductor")
    def mostrar(self):
        print("El auto muestra un interfaz donde se estan las caracteristices del auto llendo desde la velocidad hasta notificar algun fallo")
lamborghini_sesto_elemento = auto ("Lamborghini","Sesto Elemento","2011","Gris mate con acentos en color rojo","Motor v 10 Atmosferico de 5.2 litros","Automatica Robotizada e-gear de 6 velocidades","2 puertas","0 km (por ser de coleccion)","999 kg","2 personas")

lamborghini_sesto_elemento.viajar()
lamborghini_sesto_elemento.avanzar()
lamborghini_sesto_elemento.encender()
lamborghini_sesto_elemento.frenar()
lamborghini_sesto_elemento.mostrar()
