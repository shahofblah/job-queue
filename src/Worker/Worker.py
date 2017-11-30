import requests
from threading import Thread
from sys import argv, path
path.insert(0, "../Common")
from Endpoints import PORT, QUEUE_SERVER
from Resources import Resources
from Job import Job

def getAllocatedResources(args):
	return 'dummyResource'

resource = getAllocatedResources(argv[1:-1])

def free(resource):
	return True;

def execute(task):
	print('Executing task '+str(task))
	return

data = {'operation': 'pop'}
url = 'http://'+QUEUE_SERVER+':'+str(PORT)

while free(resource):
	task = requests.post(url,data).text
	print (task)
	taskThread = Thread(target=execute,args=(task,))
	taskThread.start()