class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if not self.is_empty():    
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        if not self.stack:
            return True
        return False
    
    def size(self):
        return len(self.stack)

def main():
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    print("The last element that is deleted and returned:", s.pop())
    print("The last element of the list:", s.peek())
    print("The list is empty:", s.is_empty())
    print("Numbers of elements in the list:", s.size())


if __name__ == "__main__":
    main()