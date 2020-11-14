class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty")


if __name__ == "__main__":
    stack = Stack()
    print("Is empty stack ? {}".format(stack.isEmpty()))
    print("add 0 to 9")
    for number in range(10):
        stack.push(number)

    print("stackSize: {}".format(stack.size()))
    print("peek: {}".format(stack.peek()))
    print("pop: {}".format(stack.pop()))
    print("peek: {}".format(stack.peek()))
    print("Is empty stack ? {}".format(stack.isEmpty()))
    print(stack)