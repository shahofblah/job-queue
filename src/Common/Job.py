import sys
sys.path.insert(0, "../Common")
from Resources import Resources

class Job:
	"""Class representing a runnable job"""

	#Initialise with dictionary of arguments : Docker image, cmd parameters to pass to image,
	#environment variables and resources needed
	def __init__(self, arg):
		self.res = arg['resources']
		self.cmdParam = arg['cmdParam']
		self.envVar = arg['envVar']
		self.image = arg['image']
		return

	#Get resource requirements for this job
	def getResources(self):
		return self.res

	#Runs the executor function
	#Consumes and frees the resources before and after execution respectively
	def execute(self, executor, resources):
		resources.consume(self.res)
		executor(cmdParams=self.cmdParam, envVars=self.envVar, image=self.image)
		resources.free(self.res)
		return

		