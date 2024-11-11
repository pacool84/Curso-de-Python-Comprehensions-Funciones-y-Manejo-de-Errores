items = [
  {
    'product': 'camisa',
    'price': 100
  },
  {
    'product': 'pantalon',
    'price': 120
  },
  {
    'product': 'chamarra',
    'price': 150
  } 
]

def add_taxes(item):
  new_item = item.copy() #Para que no apunten a la misma referencia en memoria, hacemos una copia de la lista de arreglo original
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items))


#El problema aqui es que MAP esta definido como inmutable sin embargo al revisar las lista "items" este si cambio lo cual NO deberia de pasar
#Lo anterior ocurre por "LA REFERENCIA EN LA MEMORIA" ya que los dos hacen referencia al mismo espacio en memoria 
print(f'ORIGINAL LIST {items}')
print(f'NEW LIST {new_items}')

