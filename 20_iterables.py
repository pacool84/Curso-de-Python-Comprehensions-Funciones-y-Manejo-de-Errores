#Recordando los iterables que hemos visto previamente

for i in range(1,11):
  print(i)

#Ahora utilizando la funcion "iter()"
my_iter = iter(range(1,11)) #Con "iter" podemos controlar un iterador de manera manual
print(my_iter) #output <range_iterator object at 0x103129cb0>

#Podemos controlar la manera en la que se ejecuta, de manera manual, se puede generar iteraciones de manera manual con "next"
#Esto lo va generando progresivamente, esto ayuda mucho en temas de performance

print(next(my_iter)) #Output 1
print(next(my_iter)) #Output 2
print(next(my_iter)) #Output 3

#Se debe de tener en cuenta que esto tiene un limite de iteracion 
my_iter_2 = iter(range(1,4))
print(next(my_iter_2))
print(next(my_iter_2))
print(next(my_iter_2))
print(next(my_iter_2)) #En esta iteracion manual enviaria un error por que el range va de 1 a 4