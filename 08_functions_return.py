#Las funciones son capaces de poder retornar valores
def my_math(text, a, b):
  multiplicacion = f'{text} {a * b}'
  return multiplicacion

the_result = my_math('El resultado de la multiplicacion es: ', 4, 2) #El "return" lo podemos recibir asignandolo a cualquier variable
print(f'Aqui recibimos el return con el valor {the_result}')

#Otro Ejemplo
def sum_with_range(start, end):
  sum = 0
  for x in range(start, end):
    sum += x
  return sum

calc1 = print(sum_with_range(0, 100))#⭐️El concepto mas importante que aprendo es que el return lo podemos recibir en una variable⭐️
calc2 = print(sum_with_range(0, 1000))
