PUSH = 'push'
POP = 'pop'

#Returns a push request containing job
def createPushRequest(job):
	#TODO
	return

#Returns a request to pop from job queue if popped value can be accommodated in resources
def createPopRequest(resources):
	#TODO
	return

#Returns the operation type, whether PUSH or POP, of a request
def getOperation(request):
	#TODO
	return

#Extracts the resources from a pop request
#Raise TypeError if request is a push request
def getResources(request):
	#TODO
	return

#Extracts the job from a push request
#Raise TypeError if request is a pop request
def getJob(request):
	#TODO
	return