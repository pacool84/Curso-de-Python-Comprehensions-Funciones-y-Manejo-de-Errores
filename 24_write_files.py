#El permiso de "r+" nos permite leer y escribir pero no sobrescribe el archivo
#El permiso de "w+" nos permite leer y escribir pero SOBRESCRIBE EL ARCHIVO
with open('./text.txt', 'r+') as file:
  for line in file:
    print(line)
  file.write('En camino a la ingenieria de software\n')