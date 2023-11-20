import requests
from sys import argv, path
import sys
path.insert(0, "../Common")
from Endpoints import PORT, QUEUE_SERVER
from QueueAPI import PUSH, createPushRequest

def taskFromArgs(args):
	return args[0]

task = taskFromArgs(argv[1:])

data = createPushRequest(task)

url = 'http://'+QUEUE_SERVER+':'+str(PORT)

request = {'data':data}
r = requests.post(url,data)
print(r.text)