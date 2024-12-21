'''
1.-Poder seleccionar la columna "World Population Percentage", columna Q
2.-Obtener todos los valores de esa columna
3.-Graficar los valores de esa columna
'''

import csv
import matplotlib.pyplot as plt

def read_csv(path):
  world_population_percentage = []
  countries = []
  with open (path, 'r+') as file:
    reader = csv.reader(file)
    next(reader)
    for column in reader:
      countries.append(column[2])
      world_population_percentage.append(float(column[16]))
      #otra manera de resolverlo sería 
      #countries_2 = list(map(lambda x: x['Country'], reader))
      #world_population_percentage_2 = list(map(lambda x: x['World Population Percentage'], reader))
    return countries, world_population_percentage
    
def graph_world_population(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  
  plt.title('World Population Percentage')
  plt.xlabel('Country')
  plt.ylabel('Percentage')
  plt.show()

countries, values = read_csv('./data.csv')
graph_world_population(countries, values)