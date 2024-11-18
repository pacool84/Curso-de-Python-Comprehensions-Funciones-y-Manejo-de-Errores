def get_population():
  key = ['col', 'mx']
  value = [2500, 35000]
  return key, value

name = 'Sebas'

def population_by_country(data, country):
  result = list(filter(lambda item : item['Country'] == country, data ))
  return result 