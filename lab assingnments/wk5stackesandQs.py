class stack:
#STACKS AND QUEUES:
     def __init__(self):
         self.theitems=list()
# returns true if the stack is empty or false otherwise.
     def isempty(self):
         return len(self)==0
#returns the number of items in the stack.
     def __len__(self):
         return len(self.theitems) 
#returns the top item o the stack without removimg it
     def peek(self):
         assert not self.isempty(), "Cannot peek at an empty stack"
         return self.theitems[-1]
#removes and returns the top item o the stack.
     def pop(self):
         assert not self.isempty(), "Cannot pop from an empty stack"
         return self.theitems.pop()
#Push an item onto the top of the stack.
     def push(self,item):
         self.theitems.append(item)
# #main program
mystack=stack()     #stack class defined
userprompt=' '
value = int(input(userprompt))
while value>=0:
     mystack.push(value)
     value=int(input(userprompt))
while not mystack.isempty():
     value=mystack.pop()
     print(value)
import queue
import collections
Lq=queue.LifoQueue(maxsize=6)
# qize() give the maxsize of the queue
print(Lq.qsize())

# Data Inserted as 9->1->2, same as Queue
Lq.put(9)
Lq.put(1)
Lq.put(2)
print("Full: ", Lq.full(), "Size: ", Lq.qsize())
# Data will be accessed in the reverse order of that of Queue
print(Lq.get(),Lq.get(),Lq.get())
print("Empty: ", Lq.empty())
#Create a deque
DeQ = collections.deque(["Mon","Tue","Wed"])
print (DeQ)
# Append to the right
print("Adding to the right: ")
DeQ.append("Thu")
print (DeQ)
# append to the left
print("Adding to the left: ")
DeQ.appendleft("Sun")
print (DeQ)
# Remove from the left
print("Removing from the left: ")
DeQ.popleft()
print (DeQ)
# Reverse the dequeue
print("Reversing the deque: ")
DeQ.reverse()
print (DeQ)
#Initializing a queue
queue = []
# Adding elements to the queue
queue.append('m')
queue.append('n')
queue.append('o')
print("Initial queue")
print(queue)
# Removing elements from the queue
print("\nElements dequeued from queue")

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)



# out put
# 1
#  2
#  3
#  4
#  5
#  6
#  7
#  8
#  9
#  -1
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# Full:  False Size:  3
# 2 1 9
# Empty:  True
# deque(['Mon', 'Tue', 'Wed'])
# Adding to the right:
# deque(['Mon', 'Tue', 'Wed', 'Thu'])
# Adding to the left:
# deque(['Sun', 'Mon', 'Tue', 'Wed', 'Thu'])
# Removing from the left:
# deque(['Mon', 'Tue', 'Wed', 'Thu'])
# Reversing the deque:
# deque(['Thu', 'Wed', 'Tue', 'Mon'])
# Initial queue
# ['m', 'n', 'o']

# Elements dequeued from queue
# m
# n
# o

# Queue after removing elements
# []
