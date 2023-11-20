import sys
sys.path.insert(0, "../src/Common")
import pytest
from QueueAPI import PUSH, POP, createPushRequest, createPopRequest, getResources, getOperation, getJobFromResponse, getJobFromRequest, createPopResponse

@pytest.fixture(scope='function')
def setup():

	global job
	global resources
	global request1
	global request2
	global response1
	global response2

	job = 'job'
	resources = 'resources'
	request1 = createPushRequest(job)
	request2 = createPopRequest(resources)
	response1 = createPopResponse(success=False, job=None)
	response2 = createPopResponse(success=True, job=job)


def test_getJobFromRequest(setup):
	assert getJobFromRequest(request1) == job

def test_getResource(setup):
	assert getResources(request2) == resources

def test_getOperationPush(setup):
	assert getOperation(request1) == PUSH

def test_getOperationPop(setup):
	assert getOperation(request2) == POP

def test_getJobFromResponse(setup):
	assert getJobFromResponse(response2) == job

def test_InvalidGetJobFromResponse(setup):
	with pytest.raises(ValueError):
		getJobFromResponse(response1)
