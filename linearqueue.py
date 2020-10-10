##Linear Queue Data Structure

#Main Queue Class
class LinearQueue():
    def __init__(self, length):
        #When initiating, user defines the length.
        #The head and tail pointers are set at -1 (i.e. not pointing to anything, index beginning at zero)
        #The queue is set as a series of None objects in a list the length the user gave
        self._length = length
        self._head = self._tail = -1
        self._queue = [None]*self._length
    def enqueue(self, *args):
        #Enqueue - Adds value to Queue (First-In)
        #Arguments are taken as a tuple of any length and are processed one at a time
        for i in args:
            if not self.isFull():
                #The queue is checked if it is full. If it isn't, the value is added to the end of the queue and the tail is updated.
                self._tail += 1
                self._queue[self._tail] = i
            else:
                #Otherwise, if the list is full, the loop breaks and no more values are taken from the arguments.
                break
    def dequeue(self):
        #Dequeue - Take value from Queue (First Out)
        if self.isEmpty() or (self._tail == self._head):
            #If the queue is empty or the head and tail point at the same position, None is returned
            return None
        else:
            #If the queue is not empty, the value being pointed to by the head pointer is returned and the head pointer shifts up one
            #To emulate a real Queue, this value is not removed, however it is ignored
            self._head += 1
            self._dequeueValue = self._queue[self._head]
            return self._dequeueValue
    def isFull(self):
        return self._tail == (self._length-1) #If the tail pointer is the same as the length (minus one) of the queue then it is full. If not, it isn't full.
    def isEmpty(self):
        return self._tail == self._head == -1 #If the head and tail pointers are both -1, then the queue is empty. If not, it isn't empty.

#Test with a Queue of Length 5 named 'q'
print("Creating Linear Queue of 5 with No Values")
q = LinearQueue(5)
print("empty",q.isEmpty())
print("Enqueuing 1, 2, 3")
q.enqueue(1, 2, 3)
print("full",q.isFull())
print("empty",q.isEmpty())
print("dequeuing 1, 2, 3")
for i in range(0,3):
    print("dequeuing",q.dequeue())
print("empty",q.isEmpty())
print("Enqueuing 4, 5")
q.enqueue(4, 5)
print("full",q.isFull())
print("empty",q.isEmpty())
print("dequeuing all")
for i in range(0,2):
    print("dequeuing",q.dequeue())
print("full",q.isFull())
print("empty",q.isEmpty())
print("dequeuing extra value (should return None)")
print("dequeuing",q.dequeue())
