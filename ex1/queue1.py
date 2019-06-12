#FIFO
import queue
q = queue.Queue(maxsize=0)
q.put_nowait("el1")
q.put_nowait("el2")
print(q.get_nowait())
print(q.get_nowait())

#LIFO
q = queue.LifoQueue()
q.put_nowait("el1")
q.put_nowait("el2")
print(q.get_nowait())
print(q.get_nowait())

#Priority
q = queue.PriorityQueue()
q.put_nowait((10,"el1"))
q.put_nowait((2,"el2"))
q.put_nowait((12,"el3"))
print(q.get_nowait())
print(q.get_nowait())
print(q.get_nowait())
