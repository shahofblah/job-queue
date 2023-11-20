import requests
from threading import Thread
from time import sleep
from sys import argv, path
path.insert(0, "../Common")
from Endpoints import PORT, QUEUE_SERVER
from Resources import Resources
from Job import Job
from QueueAPI import POP, createPopRequest, getJobFromResponse

def getAllocatedResources(args):
	res = {}
	res['cpu'] = args[0]
	res['ram'] = args[1]
	return res

def runner(cmdParams, envVars, image):
	#run task
	return

resource = getAllocatedResources(argv[1:])

data = createPopRequest(resource)
url = 'http://'+QUEUE_SERVER+':'+str(PORT)
request = {'data':data}

response = requests.post(url,request).text

#Initially run as many tasks as can be run
while (response['success'] == True):
	task = getJobFromResponse(response)
	taskThread = Thread(target=task.execute,args=(task,))
	taskThread.start()
	data = createPopRequest(resource)
	request = {'data':data}
	response = requests.post(url,request).text

sleep(5)

#Call at 5s intervals if pop unsuccessful
while(True):
	data = createPopRequest(resource)
	url = 'http://'+QUEUE_SERVER+':'+str(PORT)
	request = {'data':data}

	response = requests.post(url,request).text
	if(response['success'] == False):
		sleep(5)
	else:
		task = getJobFromResponse(response)
		taskThread = Thread(target=task.execute,args=(runner,resource,))
		taskThread.start()
