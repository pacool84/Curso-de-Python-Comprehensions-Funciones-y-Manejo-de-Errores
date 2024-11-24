#Algunos tipos de errores comunes son:

#Error de sintaxis
print(0 / 0)) #SyntaxError: unmatched ')'

#Error por division entre 0
print(0 / 0) #ZeroDivisionError: division by zero

#Error por variable NO dreclarada
print(result) #NameError: name 'result' is not defined

#Error por assert / verificar 
suma = lambda x,y : x + y
assert suma(2,2) == 4 #Aqui si se cumple el assert 
assert suma(2,3) == 4 #AssertionError, ya que no cumple con la hipostesis 

#Generar mis propias excepciones 
age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')

#Cualquiera de los errores anteriores hace que nuestro programa se detenga