class MedioTransporte :
    def __init__(self,capacidad_max,fuente_energia,via_dezplazamiento,velocidad_max,autonomia,peso,sistema_direccion,anio_fabricacion,frenado,registro):
        self.capacidad_max = capacidad_max
        self.fuente_energia = fuente_energia
        self.via_dezplazamiento = via_dezplazamiento
        self.velocidad_max = velocidad_max
        self.autonomia = autonomia
        self.peso = peso
        self.sistema_direccion = sistema_direccion
        self.anio_fabricacion = anio_fabricacion
        self.frenado = frenado
        self.registro = registro
        print(f"La capacidad maxima es de: {self.capacidad_max}")
        print(f"la fuente de energia del vehiculo es: {self.fuente_energia}")
        print(f"La via de dezplazamiento del vehiculo es: {self.via_dezplazamiento}")
        print(f"La velocidad maxima del vehiculo es de: {self.velocidad_max}")
        print(f"La autonomia del vehiculo es de: {self.autonomia}")
        print(f"El peso del vehiculo es de: {self.peso}")
        print(f"El sistema de direccion de el vehiculo es: {self.sistema_direccion}")
        print(f"El año de fabricacion de vehiculo es: {self.anio_fabricacion}")
        print(f"El sistema de frenado es: {self.frenado}")
        print(f"La manera en que se registra los vehiculos es: {self.registro}")
    def subir(self):
        print("El vehiculo puede subir pasaje")
    def llegar(self):
        print("el vehiculo es capaz de llegar en un tiempo determinado")
    def parar(self):
        print("El vehiculo se puede parar en lugares donde indique el pasaje o en un lugar ya establecido")
    def cobrar(self):
        print("En el vehiculo hay un precio por cada lugar de llegada o de subida")
    def bajar(self):
        print("una vez en el lugar de destino el pasaje baja dependiendo si es su lugar de llegada o no")
microbus = MedioTransporte ("23 Pasajeros","Gas LP","Terrestre","80 km/h","300 a 400 km","3.5 toneladas","Volante hidraulico y planca de cambios","1994","Frenos de liquido tradicionales","Numero de ruta pintado enfrente del vehiculo")

microbus.subir()
microbus.llegar()
microbus.parar()
microbus.cobrar()
microbus.bajar ()

