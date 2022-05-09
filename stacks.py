from linkedlist import LinkedList

class Stack(LinkedList):

    def push(self, value):
        self.appendRight(value)
    
    def pop(self):
        return self.popRight()

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(100)
    stack.push(9000)
    stack.print()