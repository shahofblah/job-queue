import requests
from sys import argv, path
import sys
path.insert(0, "../Common")
from Endpoints import PORT, QUEUE_SERVER

data = {'operation': argv[1], 'task': 'thisisTask'}
url = 'http://'+QUEUE_SERVER+':'+str(PORT)
r = requests.post(url,data)
print(r.text)