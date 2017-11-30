import sys
sys.path.insert(0, "../../src/Common")
import pytest
from Resources import Resources

@pytest.fixture(scope='function')
def setup():

	global resource1
	global resource2
	global resource3

	resource1 = Resources({'cpu':100, 'ram':150})
	resource2 = Resources({'cpu':50, 'ram':180})
	resource3 = Resources({'cpu':80, 'ram':100})
	return

def test_ImpossibleConsume(setup):
	#A worker with resource1 free cannot run a job requiring resource2
	with pytest.raises(ValueError):
		resource1.consume(resource2)

def test_PossibleConsume(setup):
	#A worker with resource1+resource2 free can run job requiring resource2
	resource1.free(resource3)
	resource1.consume(resource2)