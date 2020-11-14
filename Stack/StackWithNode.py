class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print(" Stack is empty")

    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print("stack is empty")

    def size(self):
        return self.count

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end= " ")
            node = node.pointer
        print()


if __name__ == "__main__":
    stack = Stack()
    print("Is empty stack ? {}".format(stack.isEmpty()))
    print("add 0 to 9")
    for number in range(10):
        stack.push(number)
    stack._printList()

    print("stackSize: {}".format(stack.size()))
    print("peek: {}".format(stack.peek()))
    print("pop: {}".format(stack.pop()))
    print("peek: {}".format(stack.peek()))
    print("Is empty stack ? {}".format(stack.isEmpty()))
    stack._printList()