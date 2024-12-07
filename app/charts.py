#utilizaremos la libreria Matplotlib para la generacion de graficos con python
#https://matplotlib.org/
#Debemos de instalar esta libreria ya que no viene por defecto en las librerias de python 
#pip install matplotlib

import matplotlib.pyplot as plt

def generate_bar_chart(labels, values): 
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()
  
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 200, 80]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)