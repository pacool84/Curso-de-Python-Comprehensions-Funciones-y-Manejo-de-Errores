#El metodo filter nos ayuda a filtar elementos de una lista
#Generalemnte, este filter debe de contar con un criterio o condicional para poder aplicar el filtrado
#Se debe considerar que un posible resultado de aplicar un filter es tener una lista "vacia"
#La lista original no puede nunca ser mayor a la lista filtrada
#Filter aplica el concepto de inmutabilidad 

numbers = [1,2,3,4,5,6,7,8,9,10]
new_numbers = list(filter(lambda numero : numero %2 == 0, numbers))#Tambien con este metodo debemos de aplicar la transformacion a lista ya que hace referencia al puntero en memoria 
print(new_numbers)