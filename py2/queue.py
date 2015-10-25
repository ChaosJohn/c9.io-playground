"""Using Lists as Queues"""
from collections import deque

QUEUE = deque(["Eric", "John", "Michael"])
print QUEUE
QUEUE.append("Terry")
QUEUE.append("Graham")
print QUEUE.popleft()
print QUEUE.popleft()
print QUEUE

