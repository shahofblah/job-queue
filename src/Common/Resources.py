class Resources:
	"""Class representing resources(CPU, memory, etc)"""

	#Initialise with dictionary containing CPU and memory
	def __init__(self, arg):
		self.res = {}
		self.res['cpu'] = arg['cpu']
		self.res['ram'] = arg['ram']
		return

	#If internal state before function call represented free resources in a worker, 
	#after function call it represents free resources once it starts executing a job 
	#with resource jobRequirement requirements
	def consume(self, jobRequirement):
		if((self.res['cpu'] < jobRequirement.res['cpu']) or (self.res['ram'] < jobRequirement.res['ram'])):
			raise ValueError
		
		self.res['cpu'] -= jobRequirement.res['cpu']
		self.res['ram'] -= jobRequirement.res['ram']
		return

	#Opposite of consume; a job with jobRequirement requirements finishes execution
	def free(self, jobRequirement):
		self.res['cpu'] += jobRequirement.res['cpu']
		self.res['ram'] += jobRequirement.res['ram']
		return

		