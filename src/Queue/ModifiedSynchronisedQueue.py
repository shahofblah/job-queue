from queue import Queue
class ModifiedQueue(Queue):
    def modGet(self, predicate):
        '''Remove and return front item from the queue if it satisfies predicate
        '''
        with self.not_empty:
            if not self._qsize():
                    raise Empty
            if predicate(self.queue[-1]):
                item = self._get()
                self.not_full.notify()
                return item
            else:
                raise ValueError
