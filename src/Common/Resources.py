class Resources:
	"""Class representing resources(CPU, memory, etc)"""

	#Initialise with dictionary containing CPU and memory
	def __init__(self, arg):
		#TODO
		return

	#If internal state before function call represented free resources in a worker, 
	#after function call it represents free resources once it starts executing a job 
	#with resource jobRequirement requirements
	def consume(self, jobRequirement):
		#TODO
		return

	#Opposite of consume; a job with jobRequirement requirements finishes execution
	def free(self, jobRequirement):
		#TODO
		return

		