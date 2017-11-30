import sys
sys.path.insert(0, "../../src/Common")
import pytest
from QueueAPI import PUSH, POP, createPushRequest, createPopRequest, getResources, getOperation, getJob
import Job
import Resources

@pytest.fixture(scope='function')
def setup():

	global job
	global resources
	global request1
	global request2

	job = 'job'
	resources = 'resources'
	request1 = createPushRequest(job)
	request2 = createPopRequest(resources)


def test_getJob(setup):
	assert getJob(request1) == job

def test_getResource(setup):
	assert getResources(request2) == resources

def test_getOperationPush(setup):
	assert getOperation(request1) == PUSH

def test_getOperationPop(setup):
	assert getOperation(request2) == POP

def test_IncorrectGetJob(setup):
	with pytest.raises(TypeError):
		getJob(request2)

def test_IncorrectGetResources(setup):
	with pytest.raises(TypeError):
		getResources(request1)