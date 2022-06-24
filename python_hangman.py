import random
import json
from urllib.request import urlopen
url = "https://www.randomlists.com/data/words.json"
response = urlopen(url)
data_json = json.loads(response.read())
print(data_json)