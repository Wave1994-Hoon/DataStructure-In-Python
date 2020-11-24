
class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()

        if value != None:
            return value

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]

    def __repr__(self):
        return repr(self.items)


if __name__ == "__main__":
    queue = Queue()
    print(f"is empty Queue ?: {queue.isEmpty()}")

    for i in range(5):
        queue.enqueue(i)
        print(f"Queue: {queue}")

    print(f"Queue size: {queue.size()}")
    print(f"peek: {queue.peek()}")

    queue.dequeue()
    print(f"Queue: {queue}")





