##Priority Queue Data Structure

#Main Queue Class
class PriorityQueue():
    def __init__(self, length):
        #When initiating, user defines the length.
        #The head and tail pointers are set at -1 (i.e. not pointing to anything, index beginning at zero)
        #The queue is set as a series of None objects in a list the length the user gave
        self._length = length
        self._head = self._tail = -1
        self._queue = [(None,0)]*self._length
    def enqueue(self, arg, priority):
        #Enqueue - Adds value to Queue (First-In)
        if not self.isFull() and type(priority) is int:
            #A new value is added if the queue is not full and the priority is a valid integer
            #Otherwise the value is ignored
            if priority > 0:
                #If the priority is greater than 0, which is the minimum value for the queue, it will be added
                self._valuesToShift = []
                self._insertPosition = None
                #An empty list is created to store the values that will be shifted along
                #A variable with 'None' in it will be used to store the index of which the new argument is added
                for i in self._queue:
                    #Every value of the queue is examined one at a time
                    if i[1] < priority:
                        if i[1] > 0:
                            self._valuesToShift.append(i)
                            #If the priority of the value is greater than 0 and less than the priority, the value is noted appropriately to be shifted
                        if self._insertPosition == None:
                            self._insertPosition = self._queue.index(i)
                            #The insert position is updated to the index of the first value with less priority than the new argument
                self._queue[self._insertPosition] = (arg, priority)
                #The queue is updated so that the new argument is added to it's relevant position
                for i in self._valuesToShift:
                    self._insertPosition += 1
                    self._queue[self._insertPosition] = i
                    #Then, the rest of the values are shifted along
                self._tail += 1
                #Finally the tail is incremented by one
    def dequeue(self):
        #Dequeue - Take value from Queue (First Out)
        if self.isEmpty() or (self._tail == self._head):
            #If the queue is empty or the head and tail point at the same position, None is returned
            return None
        else:
            #If the queue is not empty, the value being pointed to by the head pointer is returned and the head pointer shifts up one
            #To emulate a real Queue, this value is not removed, however it is ignored
            self._head += 1
            self._dequeueValue = self._queue[self._head][0]
            return self._dequeueValue
    def isFull(self):
        return self._tail == (self._length-1) #If the tail pointer is the same as the length (minus one) of the queue then it is full. If not, it isn't full.
    def isEmpty(self):
        return self._tail == self._head == -1 #If the head and tail pointers are both -1, then the queue is empty. If not, it isn't empty.

#Test with a Queue of Length 5 named 'q'
print("Creating Priority Queue of 5 with No Values")
q = PriorityQueue(5)
print("empty",q.isEmpty())
print("enqueuing ('Matt',4), ('James',1) and ('John',2)")
q.enqueue('Matt', 4)
q.enqueue('James', 1)
q.enqueue('John', 2)
print("full",q.isFull())
print("empty",q.isEmpty())
print("enqueuing ('Emma', 2) and ('Jackson', 3)")
q.enqueue('Emma', 2)
q.enqueue('Jackson', 3)
print("full",q.isFull())
print("empty",q.isEmpty())
print("dequeuing first 3 values")
for i in range(0,3):
    print("dequeued",q.dequeue())
print("full",q.isFull())
print("empty",q.isEmpty())
print("dequeuing 4th and 5th values")
for i in range(0,2):
    print("dequeued",q.dequeue())
print("full",q.isFull())
print("empty",q.isEmpty())
print("dequeuing extra value (should return None)")
print("dequeuing",q.dequeue())
