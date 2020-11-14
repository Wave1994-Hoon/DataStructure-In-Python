class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack(object):
    def __init__(self):
        self.head = None  # head : Stack의 가장 윗 부분을 가리킴
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    ''' 
    1. newNode는 기존에 존재하는 이전 Node(head)를 가리킴         
    2. head는 newNode를 가리킴
    '''
    def push(self, item):
        newNode = Node(item, self.head)
        newNode.next = self.head
        self.head = newNode
        self.count += 1

    '''
    1. value에 head.value를 담음 
    2. head에는 이전 노드주소(head.next)를 담음
    '''
    def pop(self):
        if self.count > 0 and self.head:
            value = self.head.value
            self.head = self.head.next
            self.count -= 1
            return value
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
            print(node.value, end=" ")
            node = node.next
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
