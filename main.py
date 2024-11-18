#Una forma similar para importar la carpeta "package" es la siguiente:
#import packages

#Utilizaremos una sintaxis mas moderna, a esto se le conoce como "import explicito"
'''from packages.mod_1 import func_1, func_2
import packages.mod_1
from packages.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())'''

#Cada ves que se ejecute este archivo "main.py" el archivo "__init__.py" tambien se inicializara una vez
#Por lo anterior tambien es posible realizar llamados directos a las variables que se encuentren en "__init__.py"
import packages
print(f'Esta es una variable desde __init__py ==> {packages.URL}') #Recuerda que esto es para las versiones antes de la 3.3 en python 

#Ahora trabajaremos con importacion  "NAMESPACES"
#El siguiente ejemplo es en caso de que no utilicemos la importacion explicita "from packages.mod_1 import func_1, func_2"
#Es necesario que bajo esta situacion / contexto se haga la importacion del paquete y del modulo desde el archivo __init__.py

print(packages.mod_1.func_1())
