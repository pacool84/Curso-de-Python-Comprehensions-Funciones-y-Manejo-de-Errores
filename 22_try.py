#Debemos de procurar hacer el correcto manejo de errores, para evitar que el programa se detenga
try:
  print(0 / 0)
except ZeroDivisionError as error:
  print(f'Se identifico un error en el programa: " {error} "')
  
print('Se valida que el programa continua')

#Una buena practica en ingenieria es hacre tracking de los errores en un sistema aparte

#Captura de otro tipo de error 
try:
  assert 1 != 1, 'Uno NO es igual a uno'
except AssertionError as error:
  print(f'Se indentifico un error en el programa: " {error} "')

print('Se valida que el programa continua')

#Captura de una excepcion o error propio
try:
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except Exception as error:
  print(f'Se identifico una excepcion en el programa: " {error}  "')

print('Se valida que el programa continua')

#una forma recomendable de hacer el manejo de error mas extensivo es utilizando el sig esquema 
print('##############Esquema Recomendable para el manejo de errores##############')
try:
  #Primero que se ejecute la logica del programa
  assert 1 != 1, 'Uno NO es igual a uno'
  
  print(0 / 0)
  
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')

 #Segundo que se validen los posibles errores del programa
except ZeroDivisionError as error:
  print(f'Se identifico un error en el programa: " {error} "')
except AssertionError as error:
  print(f'Se indentifico un error en el programa: " {error} "')
except Exception as error:
  print(f'Se identifico una excepcion en el programa: " {error}  "')

print('Se valida que el programa continua')