from linkedlist import LinkedList

class Queue(LinkedList):

    def enqueue(self, element):
        self.appendRight(element)
    
    def dequeue(self):
        return self.popLeft()


if __name__ == '__main__':
    q = Queue()
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    q.print()

    q.dequeue()
    q.dequeue()
    q.print()
    q.dequeue()
    q.print()
    q.dequeue()