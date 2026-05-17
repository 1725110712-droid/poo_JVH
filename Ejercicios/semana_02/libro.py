class LibroDeBiblioteca:
    def __init__(self,pasta,cantidad_de_hojas,numero_de_id,autor,genero,editorial,idioma,anio_de_edicion,material,numero_de_tomo):
        self.pasta = pasta
        self.cantidad_de_hojas = cantidad_de_hojas
        self.numero_de_id = numero_de_id
        self.autor = autor 
        self.genero = genero 
        self.editorial = editorial  
        self.idioma = idioma
        self.anio_de_edicion = anio_de_edicion 
        self.material = material
        self.numero_de_tomo = numero_de_tomo
        print(f"tipo de pasta: {self.pasta}")
        print(f"la cantidad de hojas es : {self.cantidad_de_hojas}")
        print(f"El numero de identificacion es: {self.numero_de_id}")
        print(f"El autor es: {self.autor}")
        print(f"El genero del libro es: {self.genero}")
        print(f"La editorial es: {self.editorial}")
        print(f"El idioma original del libro es: {self.idioma}")
        print(f"El año de edicion es: {self.anio_de_edicion}")
        print(f"El material del que esta hecho el libro es: {self.material}")
        print(f"El numero de tomo es: {self.numero_de_tomo}")
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
el_libro_de_urantia = LibroDeBiblioteca("Pasta dura","1,048 hojas","978-1883395216","Anonimo","Religion y cosmologia","Urantia Foundation","Ingles","1955","Cubiertas de carton y hojas de papel biblia","Volumen unico")

el_libro_de_urantia.entretener()
el_libro_de_urantia.leer()
el_libro_de_urantia.educar()
el_libro_de_urantia.cuidar()
el_libro_de_urantia.imaginar()



