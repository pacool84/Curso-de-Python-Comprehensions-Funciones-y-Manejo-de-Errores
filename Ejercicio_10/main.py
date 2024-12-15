'''
1.- Poder Seleccionar un país
2.-Identificar la poblacion por año de ese pais en el archivo
'''

import csv
import matplotlib.pyplot as plt

def read_csv(path, country):
  with open(path, 'r+') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
      if row[2] == country:
        population = list(map(int, row[5:12]))
        return headers[5:12], population
        
def graph_population(labels, values):
  fig, ax = plt.subplots()
  bars = ax.bar(labels, values)
  
  for bar in bars:
        height = bar.get_height()  # Obtiene la altura de cada barra
        ax.text(
            bar.get_x() + bar.get_width() / 2,  # Posición X: Centro de la barra
            height - (height * 0.05),  # Posición Y: Un poco debajo del tope de la barra
            f'{height:,}',  # Texto con formato numérico
            ha='center', va='center', fontsize=10, color='black'
        )
        
  plt.title(f'Tendencia de población')
  plt.xlabel('Año')
  plt.ylabel('Poblacion')
  plt.show()
  
  

user_option = input('Dime el país: ').capitalize()
headers, values = read_csv('./data.csv', user_option)
graph_population(headers, values)
