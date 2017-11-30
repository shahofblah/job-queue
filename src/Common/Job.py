class Job:
	"""Class representing a runnable job"""

	#Initialise with dictionary of arguments : Docker image, cmd parameters to pass to image,
	#environment variables and resources needed
	def __init__(self, arg):
		#TODO
		return

	#Get resource requirements for this job
	def getResources(self):
		#TODO
		return

	#Runs the executor function
	#Consumes and frees the resources before and after execution respectively
	def execute(self, executor, resources):
		#TODO
		return

		