'''
Una función es un bloque de código reutilizable que realiza una tarea específica.
Las funciones nos permiten evitar la repetición de código y organizan el código en unidades lógicas, mejorando la legibilidad y la eficiencia.

La estructura básica de una función en Python es:
	•	def: Palabra clave para definir una función.
	•	nombre_funcion: El nombre que le damos a la función.
	•	parametros: Valores que recibe la función para operar (opcionales).
	•	return: Devuelve un valor como resultado de la función (opcional).
'''

# Definición de una función llamada 'my_function' que toma dos parámetros: 'a' y 'b'
def my_function(a, b):
    # Imprime un mensaje para indicar que se está ejecutando la función
    print('Esta es mi función de Imprimir')
    
    # Calcula la suma de los dos parámetros 'a' y 'b' y la almacena en la variable 'suma'
    suma = a + b
    
    # Imprime el resultado de la suma usando una cadena formateada
    print(f'La suma es de {suma}')

# Llamada a la función 'my_function' pasando 4 y 5 como argumentos
my_function(4, 5)

#Ejemplo de Función con Valor de Retorno

def suma(a, b):
    resultado = a + b
    return resultado

# Llamada a la función y almacenamiento del valor retornado
resultado_suma = suma(4, 5)
print(f"El resultado de la suma es: {resultado_suma}")

#Funciones con Parámetros Opcionales (Valores Predeterminados)
def saludo_con_opcion(nombre, mensaje="¡Buen día!"):
    print(f"{mensaje} {nombre}")

# Llamadas a la función
saludo_con_opcion("Ana")  # Usará el mensaje por defecto
saludo_con_opcion("Pedro", "¡Hola y bienvenido!")  # Usa un mensaje personalizado