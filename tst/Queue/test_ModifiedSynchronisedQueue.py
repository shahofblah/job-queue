from time import sleep
from threading import Thread
import pytest
import sys
sys.path.insert(0, "../src/Queue")
from ModifiedSynchronisedQueue import ModifiedQueue

def predicate(x):
	return x<5

@pytest.fixture(scope='function')
def setup():

	global queue
	queue = ModifiedQueue()
	return

def test_Pop(setup):
	queue.put(3)
	assert queue.modGet(predicate) == 3

def test_ImpossiblePop(setup):
	queue.put(7)
	with pytest.raises(ValueError):
		queue.modGet(predicate)