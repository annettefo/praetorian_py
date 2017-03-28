import requests, json, sys
if sys.version_info < (3,0):
  sys.exit('Python version < 3.0 does not support modern TLS versions. You will have trouble connecting to our API using Python 2.X.')
email = 'annettefonta@gmail.com' # Change this!
r = requests.post('https://mastermind.praetorian.com/api-auth-token/', data={'email':email})
r.json()
# > {'Auth-Token': 'AUTH_TOKEN'}
headers = r.json()
headers['Content-Type'] = 'application/json'

# Interacting with the game
r = requests.get('https://mastermind.praetorian.com/level/1/', headers=headers)
r.json()
# > {'numGladiators': 4, 'numGuesses': 8, 'numRounds': 1, 'numWeapons': 6}
r = requests.post('https://mastermind.praetorian.com/level/1/', data=json.dumps({'guess':[1,2,3,4]}), headers=headers)
r.json()
# > {'response': [2, 1]}
