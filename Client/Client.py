import requests
from sys import argv, path
import sys
path.insert(0, "../Common")
from Endpoints import PORT, QUEUE_SERVER

def taskFromArgs(args):
	return args[0]

data = {'operation': 'push', 'task': taskFromArgs(argv[1:])}
url = 'http://'+QUEUE_SERVER+':'+str(PORT)
r = requests.post(url,data)
print(r.text)