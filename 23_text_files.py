file = open('./text.txt')
#print(file.read())

#Leer linea por linea / como un iterador 
print(file.readline())
print(file.readline())
print(file.readline())

#Cerrar el archivo
#file.close()

#Leer linea por linea del archivo / mejor practica ya que no ocupamos tanta memoria

for line in file:
  print(line)
  
#Utilizando una sintaxis mas moderna
#Esta sintaxis nos ayuda a cerrar los archivos cada vez que los dejemos de usar

with open('./text.txt') as file:
  for line in file:
    print(line)