class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.next = node
            self.tail = node
        self.count += 1


    def dequeue(self):


    def size(self):


    def peek(self):


    def __repr__(self):



if __name__ == "__main__":
    queue = LinkedQueue()
    print(f"is empty Queue ?: {queue.isEmpty()}")

    for i in range(5):
        queue.enqueue(i)
        print(f"Queue: {queue}")

    print(f"Queue size: {queue.size()}")
    print(f"peek: {queue.peek()}")

    queue.dequeue()
    print(f"Queue: {queue}")





