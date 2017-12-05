import tornado.ioloop
import tornado.web
from tornado import gen
from queue import Queue, Empty
import sys
sys.path.insert(0, "../Common")
from Endpoints import PORT
from ModifiedSynchronisedQueue import ModifiedQueue

tasks = ModifiedQueue()

class Handler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		self.write("\nQueueSize="+str(tasks.qsize()))
		return

	@gen.coroutine
	def post(self):
		if(self.get_argument('operation')=='push'):
			task = self.get_argument('task')
			tasks.put(task)
			self.write('Successfully pushed task : '+task)
		elif(self.get_argument('operation')=='pop'):
			try:
				self.write(tasks.modGet(False))
			except Empty:
				self.write('No tasks in queue')
		else:
			self.write('Invalid operation')
		return

def make_app():
	return tornado.web.Application([
		(r"/", Handler)
	])


app = make_app()
app.listen(PORT)
tornado.ioloop.IOLoop.current().start()