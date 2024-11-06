price = 100 #Esta es una variable del scope global 

print(f'Este es el precio de la variable global {price}')

def cash_salary():
  price_localFunction = 200 #Esta es una variable de scope local, de la propia funcion 
  price_local = price_localFunction + 500
  return price_local

price_local = cash_salary()
print(f'Este es el precio de la variable local, scope de la funcion cash_salary() {price_local}')

print(price_localFunction) #Esto nos daria un error de "NameError: name 'price_localFunction' is not defined" ya que esa variable esta fuera del contexto que se pueda alcanzar