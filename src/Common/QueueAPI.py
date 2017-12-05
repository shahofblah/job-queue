PUSH = 'push'
POP = 'pop'

#Returns a push request containing job
def createPushRequest(job):
	request = {}
	request['op'] = PUSH
	request['payload'] = job
	return request

#Returns a request to pop from job queue if popped value can be accommodated in resources
def createPopRequest(resources):
	request = {}
	request['op'] = POP
	request['payload'] = resources
	return

#Returns the operation type, whether PUSH or POP, of a request
def getOperation(request):
	return request['op']

#Extracts the resources from a pop request
#Raise TypeError if request is a push request
def getResources(request):
	return request['payload']

#Extracts the job from a push request
#Raise TypeError if request is a pop request
def getJobFromRequest(request):
	return request['payload']

#Returns response to pop request, containing job if pop was successful
def createPopResponse(success=False, job=None):
	response = {}
	response['success'] = success
	response['job'] = job
	return response

#Returns job if response contains it otherwise raises ValueError
def getJobFromResponse(response):
	if (response['success'] == False):
		raise ValueError
	return response['job']