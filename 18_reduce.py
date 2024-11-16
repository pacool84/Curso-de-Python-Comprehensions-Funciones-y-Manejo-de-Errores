#REDUCE nos sirve para trabajar con listas y poder reducirlas a un unico valor o conclusion
#Para utilizar REDUCE es necesario importarlo como "import functools"
#REDUCE solo retorna un valor 

import functools
numbers = [2,4,6,8,10]
#Realizaremos la sumatoria de la lista "numbers"
result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)

#Para entender de mejor manera lo anterior, cambiaremos a una funcion comun 

def acumm(counter, item):
  print(f'El counter en esta iteracion es: {counter}')
  print(f'El item en esta iteracion es: {item}')
  return counter + item

result_2 =functools.reduce(acumm, numbers)