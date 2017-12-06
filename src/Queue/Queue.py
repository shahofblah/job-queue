import tornado.ioloop
import tornado.web
from tornado import gen
from queue import Queue, Empty
import sys
sys.path.insert(0, "../Common")
from Endpoints import PORT
from ModifiedSynchronisedQueue import ModifiedQueue
from QueueAPI import PUSH, POP, getResources, getOperation, getJobFromRequest, createPopResponse

#Stores enqueued tasks
tasks = ModifiedQueue()

def requestProcessor(request):
	if(getOperation(request) == PUSH):
		task = getJobFromRequest(request)
		tasks.put(task)
		return 'Successfully pushed task : '+task
	elif(getOperation(request) == POP):
		try:
			#pops a task iff worker resources can accommodate the popped task
			return createPopResponse(success=True, job=tasks.modGet(getResources(request).canAccommodate))
		except (Empty, ValueError):
			return createPopResponse(success=False)
	else:
		return 'Invalid operation'
	return

class Handler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		self.write("\nQueueSize="+str(tasks.qsize()))
		return

	@gen.coroutine
	def post(self):
		self.write(requestProcessor(sef.get_argument['data']))
		return

def make_app():
	return tornado.web.Application([
		(r"/", Handler)
	])


app = make_app()
app.listen(PORT)
tornado.ioloop.IOLoop.current().start()