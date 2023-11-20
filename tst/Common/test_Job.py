from time import sleep
from threading import Thread, active_count
import pytest
import sys
sys.path.insert(0, "../src/Common")
from Job import Job
from Resources import Resources

def executor(cmdParams=None, envVars=None, image=None):
	sleep(1)
	return

@pytest.fixture(scope='function')
def setup():

	global resource1
	global resource2
	global resource3
	global job

	resource1 = Resources({'cpu':100, 'ram':100})
	resource2 = Resources({'cpu':200, 'ram':200})
	resource3 = Resources({'cpu':300, 'ram':300})

	param = {}
	param['resources'] = resource2
	param['cmdParam'] = None
	param['envVar'] = None
	param['image'] = None
	job = Job(param)
	return

def test_GetResource(setup):
	assert job.getResources() == resource2

#When resource requirements exceeds worker's free resources
def test_ExecutionFailure(setup):
	with pytest.raises(ValueError):
		job.execute(executor, resource1)

#When execution is successful
def test_ExecutionSuccess(setup):
	jobThread = Thread(target=job.execute, args=(executor, resource3,))
	jobThread.start()
	assert active_count() == 2
	#Free CPU and memory of resource 3 is now 100 each so resource2 worth of resources should not be consumable
	with pytest.raises(ValueError):
		resource3.consume(resource2)

	#Wait for job to finish
	jobThread.join()

	#Check if resources released
	resource3.consume(resource2)

