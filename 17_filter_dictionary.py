#Ahora trabajaremos el metodo FILTER con lista de diccionarios 

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

#Se hara el filtrado de aquellos partidos donde el equipo local haya ganado

home_wins = list(filter(lambda match : match['home_team_result'] == 'Win', matches))
print(home_wins, f'Partidos ganados por equipo local {len(home_wins)}')