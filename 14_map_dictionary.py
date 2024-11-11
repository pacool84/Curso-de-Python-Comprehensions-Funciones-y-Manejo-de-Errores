#Ahora trabajaremos MAP con una estructura de datos como lista de diccionarios

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

#Ahora realizaremos la transformacion para que sea solo la lista de precios

prices = list(map(lambda precio : precio['price'], items))
print(prices)

#Ahora realizaremos la transformacion para que sea solo la lista de productos
name_product = list(map(lambda nombre : nombre['product'], items))
print(name_product)

#Ahora agregaremos un elemento nuevo a la lista de diccionarios 
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items)

#Agreguemos el precio total del articulos 

def total_value(new_item):
 new_item['total'] = new_item['taxes'] + new_item['price']
 return new_item

total_values = list(map(total_value, new_items))
print(total_values)