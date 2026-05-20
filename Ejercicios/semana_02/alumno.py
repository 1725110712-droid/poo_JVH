class Alumno:
    def __init__(self,nombre,matricula,edad,grado,materias,historial_calificaciones,asistencias,estado,beca,datos_contacto):
        self.nombre = nombre
        self.matricula = matricula
        self.edad = edad
        self.grado = grado
        self.materias = materias
        self.historial_calificaciones = historial_calificaciones
        self.asistencias = asistencias
        self.estado = estado
        self.beca = beca
        self.datos_contacto = datos_contacto
        print(f"el nombre del alumno es: {self.nombre}")
        print(f"la matricula del alumno es: {self.matricula}")
        print(f"la edad del alumno es: {self.edad}")
        print(f"el grado del alumno es: {self.grado}")
        print(f"las materias que cursa el alumno es: {self.materias}")
        print(f"el historial de calificaciones es: {self.historial_calificaciones}")
        print(f"el porcentaje de asistencias del alumno es: {self.asistencias}")
        print(f"el estado del alumno es: {self.estado}")
        print(f"el alumno tiene beca: {self.beca}")
        print(f"los datos de contacto del alumno son: {self.datos_contacto}")
        def inscribir(self):
            print("el alumno puede inscribirse para seguir con sus estudios")
        def entregar(self):
            print("el alumno puede entregar la terea")
        def calcular(self):
            print("el alumno puede hacer calculos")
        def solicitar(self):
            print("el alumno puede solicitar tutorias para reforsar sus conocimientos")
        def registrar(self):
            print("el alumno puede registrar su asistencia en cuanto llegue a su salon")
alumno_2 = Alumno ("Edgar Alamboa","178922","19 años","3 cuatrimestre","Programacion,Calculo,Estadistica","9.8,8.5,7.8,8.3","95%","Regular","No tiene","numero de padre,numero de madre y contacto de emergencia")

alumno_2.inscribir()
alumno_2.entregar()
alumno_2.calcular()
alumno_2.solicitar()
alumno_2.registrar()          