from collections import deque
from copy import deepcopy

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def copy(self):
        new_queue = Queue()
        new_queue.items = deepcopy(self.items)
        return new_queue
    
    def __str__(self):
        return str(list(self.items))