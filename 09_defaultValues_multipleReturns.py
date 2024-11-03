def find_volume(length = 10, width = 1, depth = 1): #Al igualar los parametros que recibe nuestra funcion hacemos que se definan como valores DEFAULT
  return length * width * depth

result = find_volume()
print(result)

#En caso de que quisieramos enviar solo un parametro, pudieramos especificarlo cuando mandamos llamar a la funcion 
#Ejemplo 

def find_volume2(alto = 1, ancho = 1, profundidad = 1):
  return alto * ancho * profundidad

result2 = find_volume2(profundidad= 20)
print(result2)

#Una funcion es capaz de retornar / "return" multiples valores
#Ejemplo

def multiple_returns(parametro1, parametro2):
  text = 'Hola Multiple Return'
  return parametro1 + parametro2, text #Al regresar multiples valores, la estructura de estos datos es una "tupla"

result3 = multiple_returns(34, 40)
print(f'{result3[1]}, el resultado es {result3[0]}')  
print(type(result3))#El tipo es "tuple"