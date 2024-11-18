import utils #Es el llamado a nuestro archivo mod que esta en esta misma carpeta

data = [
    {
      'Country': 'Mexico',
      'Population': 450000
    },
    {
      'Country': 'Colombia',
      'Population': 34566
    },
    {
      'Country': 'Argentina',
      'Population': 9666
    }
  ]

#Para poder evitar un mal comportamiento de "modulos"
#Crearemos una funcion "run" que maneje la logica de esta parte
def run():
  call_module = utils.get_population() #mandamos llamar la funcion "get_population()" que esta en nuestro modulo creado
  print(call_module)
  
  #Tambien podemos mandar llamar variables
  print(f'Hola {utils.name}')

  country = input('Type Country: ')
  get_population = utils.population_by_country(data, country)
  print(get_population)
  
  #Para poder tener "dualidad" en el sentido de no depender de la 
  #la ejecucion de example.py podemos hacer un "if" que identifique 
  #si desde consola queremos ejecutar el archivo "main.py"
  
if __name__ == '__main__':
  run()