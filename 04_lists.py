#El concepto de list comprehnesion es una manera de crear o escribir listas de una manera mas facil y sencilla (sintaxis)
numbers = []

for element in range(1,101):
  numbers.append(element)
  
print(numbers)

#Ahora utilizando list comprehension
#Esto tiene como ventaja una sintaxis mas corta
#Es mas facil de entender
#La sintaxis es:
'''
[element for element in iterable]
'''
more_numbers = [element for element in range(1,101)]
print(more_numbers)

#Agregando una operacion matematica a una list comprehension

list_math = [element * 2 for element in range(1,101)]
print(list_math)

#Utilizando condicionales en un list comprenhension
#La sintaxis es:
'''
element for element in "iterable" if "condition"
'''
numbers = []
for i in range(0,11): #Forma clasica
  if i % 2 == 0:
    numbers.append(i)
print(numbers)

more_numbers = [i for i in range(0, 11) if i % 2 == 0] #Forma de list comprehension
print(more_numbers)
