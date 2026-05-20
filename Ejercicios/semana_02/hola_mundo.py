class NombreClase:
    def __init__(self):
        print("Constructor")
    def metodoUno(self): 
        print("Metodo uno")
    
    def metodoDos(self,variable_uno:int, variable_dos:int)->int:
        """
        Este metodo recibe 2 variables enteras, las suma y regresa el resultado de la suma
        
        Args:

        variable_uno : int -primer numero entero
        variable_dos : int -segundo numero entero

        Return:

        suma :int - SUma de los dos numeros
        """ 


nombre_objeto = NombreClase() 
nombre_objeto.metodoUno() 

    