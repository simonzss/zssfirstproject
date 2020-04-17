from multiprocessing import Queue

q=Queue(5)

q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.qsize())
# q.put('F') q的上限为5个，如果有第六个'F',Queue队列就会一直等待，直到前5个有一个被取走后才能put进第六个'F'
q.put('F',timeout=3) #