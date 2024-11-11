#Higher Order Functions
#Funciones de orden superior 
#Una funcion dentro de otra funcion

def increment(x):
  return x + 1

def high_ord_func(x, anotherFunction):
  return x + anotherFunction(x)

result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)

#Uno de los beneficios de HOF es poder usar lambdas o declarar funciones de una manera mas facil

incrementv2 = lambda x : x + 1 

high_ord_funcV2 = lambda x, oneMoreFunction : x + oneMoreFunction(x)

result2 = incrementv2(2)
result3 = high_ord_funcV2(2, incrementv2)

print(result2)
print(result3)