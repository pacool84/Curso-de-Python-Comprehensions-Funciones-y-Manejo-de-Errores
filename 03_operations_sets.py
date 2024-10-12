set_a = {'col', 'mx', 'bol'}
set_b = {'pe', 'bol'}

#Union de sets
set_c = set_a.union(set_b)
print(set_c)

set_family1 = {'sebas', 'bren', 'Paco'}
set_family2 = {'sebas', 'natalia'}
join_familiy = set_family1.union(set_family2)
print(join_familiy)

#Otra forma de unir sets
set_d = set_a | set_b # El simbolo "|" representa la union de conjuntos o sets
print(set_d)

#Interseccion de sets, elementos que comparten los conjuntos
set_e = set_a.intersection(set_b)
print(set_e)

#Otra forma de hacer intersecciones de sets 
set_x = set_a & set_b
print(set_x)

#Diferencia o resta en Sets
set_difference = set_a.difference(set_b)
print(set_difference)

set_difference_b = set_b.difference(set_a)
print(set_difference_b)

#Otra Forma de hacer diferencias entre sets 
set_other_difference = set_a - set_b
print(set_other_difference)

#Diferencia Simetrica, es la union de los elementos en los conjuntos sin considerar aquellos en comun 
set_difference_symmetric = set_a.symmetric_difference(set_b)
print(set_difference_symmetric)

#Otra forma de hacer diferencias simetricas

set_difference_symmetric = set_a ^ set_b