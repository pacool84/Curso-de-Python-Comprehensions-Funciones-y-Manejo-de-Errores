import csv  # Módulo nativo de Python para trabajar con archivos CSV.

# Función para leer un archivo CSV y convertirlo en una lista de diccionarios.
def read_csv(path):
    # Abrimos el archivo CSV en modo lectura.
    with open(path, 'r') as csvfile:
        # Creamos un objeto reader para procesar el archivo.
        # El delimitador se establece como ',' para archivos CSV estándar.
        reader = csv.reader(csvfile, delimiter=',')
        
        # Obtenemos el encabezado (primera línea del archivo), que contiene los nombres de las columnas.
        get_header = next(reader)
        
        # Lista donde almacenaremos los datos procesados.
        data = []
        
        # Iteramos sobre cada línea restante en el archivo.
        for line in reader:
            # Usamos zip para combinar los encabezados con los valores de la línea actual.
            # Esto genera pares clave-valor para cada columna y su dato correspondiente.
            iterable = zip(get_header, line)
            
            # Convertimos los pares clave-valor en un diccionario.
            data_as_dictionary = {key: value for key, value in iterable}
            
            # Agregamos el diccionario generado a la lista de datos.
            data.append(data_as_dictionary)
        
        # Retornamos la lista completa de diccionarios.
        return data

# Punto de entrada principal del script.
if __name__ == '__main__':
    """
    Este bloque se ejecuta solo si el script se ejecuta directamente
    (no si se importa como un módulo en otro script).
    """
    # Llamamos a la función `read_csv` pasando la ruta de un archivo CSV.
    data = read_csv('./data.csv')
    
    # Mostramos los datos leídos. 
    # Puedes descomentar la línea siguiente para inspeccionar solo el primer elemento.
    # print(data[0]) 
    print(data)