##Circular Queue Data Structure

#Main Queue Class
class CircularQueue():
    def __init__(self, length):
        #When initiating, user defines length.
        #The head and tail pointers are set at -1 (i.e. not pointing to anything, index beginning at zero)
        #A buffer is kept to track the distance between the head and the tail
        #The queue is set as a series of None objects in a list the length the user gave
        self._length = length
        self._head = self._tail = -1
        self._buffer = 0
        self._queue = [None]*self._length
    def enqueue(self, *args):
        #Enqueue - Adds value to Queue (First-In)
        #Arguments are taken as a tuple of any length and are processed one at a time
        for i in args:
            if not self.isFull():
                #The queue is checked if it is full. If it isn't, the value is added to the value after the tail and the tail is updated
                #The buffer is also updated to it's appropriate value
                self._tail = (self._tail+1)%self._length
                self._buffer += 1
                self._queue[self._tail] = i
            else:
                #Otherwise, if the list is full, the loop breaks and no more values are taken from the arguments
                break
    def dequeue(self):
        #Dequeue - Takes value from Queue (First Out)
        if self.isEmpty():
            #If the queue is empty, None is returned
            return None
        else:
            #If the queue is not empty, the value being pointed to by the head pointer is returned and the head pointer shifts up
            #To emulate a real Queue, this value is not removed, however it is ignored and can be overwritten
            #The buffer is also updated to it's appropriate vale
            self._head = (self._head+1)%self._length
            self._buffer -= 1
            self._dequeueValue = self._queue[self._head]
            return self._dequeueValue
    def isFull(self):
        return self._buffer == self._length #If the buffer is equivalent to the length of the list, the queue must be full
    def isEmpty(self):
        return self._buffer == 0 #If the buffer is 0, then the queue must be empty

#Test with a Queue of Length 5 named 'q'
print("Creating Linear Queue of 5 with No Values")
q = CircularQueue(5)
print("empty",q.isEmpty())
print("full",q.isFull())
print("enqueuing 1, 2, 3")
q.enqueue(1, 2, 3)
print("full",q.isFull())
print("empty",q.isEmpty())
print("dequeuing 1, 2, 3")
for i in range(0,3):
    print("dequeuing",q.dequeue())
print("empty",q.isEmpty())
print("Enqueuing 4, 5, 6, 7, 8")
q.enqueue(4, 5, 6, 7, 8)
print("full",q.isFull())
print("empty",q.isEmpty())
print("dequeuing all")
for i in range(0,5):
    print("dequeuing",q.dequeue())
print("full",q.isFull())
print("empty",q.isEmpty())
print("dequeuing extra value (should return None)")
print("dequeuing",q.dequeue())
