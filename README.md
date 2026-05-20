# Repositorio de Programacion Orientada a Objetos con Python

Repositorio con ejercicios de Programación Orientada a Objetos

## 1. Crear .gitignore 

Crear el archivo .gitignore para configurar los archivos y carpetas que no deseamos que se guarden en el repositorio

````shell
*.pyc
__pycache__/
````

## 2. Indexar archivos y carpetas

indexa todos los directorios en carpetas en busca de documentos nuevos

````shell 
git add .
````

## 3. Crear un COMMIT 

Crear un Commit o punto de control de los cambios realizados en el proyecto

````shell
git commit -m "Created gitignore"
````

* CREATED - Se crearon nuevas carpetas o archivos 
* UPDATED - Se actualizaron o agregaron nuevas funciones 
* FIXED - Se corrigieron errores 

## 4. Realizar el COMMIT

Sincroniza los cambios realizados en el repositorio

````shell
git push -u origin main 
````
## 5. Agregar documentación a los métodos
Agregar un **docstring** a los metodos generados 
````shell
def metodoDos(self,variable_uno:int, variable_dos:int)->int:
        """
        Este metodo recibe 2 variables enteras, las suma y regresa el resultado de la suma
        
        Args:

        variable_uno : int -primer numero entero
        variable_dos : int -segundo numero entero

        Return:

        suma :int - SUma de los dos numeros
        """ 
 ````
Sirve como una especie de manual o bitácora para tu codigo o software esto te permitira entender tus codigos rapidamente sobre todo cuando el trabajo es en equipo