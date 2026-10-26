import urllib.request
import json

pyynto = urllib.request.urlopen("https://users.metropolia.fi/~peterh/kurssit.json")
data = json.loads(pyynto.read())
print(data)
