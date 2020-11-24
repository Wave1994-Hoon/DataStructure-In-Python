'''
- 참고 자료 : https://www.youtube.com/watch?v=t45d7CgDaDM
- 스택 두개를 사용해서 큐 구현
    - inStack : input 값 받음
    - outStack : peek / dequeue 호출 시 데이터 반환, 만약 비어있다면 inStack으로 부터 데이터 받음
                (마지막으로 들어온 데이터를 먼저 넣음)
'''


class Queue(object):
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def _transfer(self):
        while self.inStack:
            self.outStack.append(self.inStack.pop())

    def isEmpty(self):
        return not (bool(self.inStack)) or (bool(self.outStack))

    def enqueue(self, item):
        return self.inStack.append(item)

    def dequeue(self):
        if not self.outStack:
            self._transfer()
        if self.outStack:
            return self.outStack.pop()

    def size(self):
        return len(self.inStack) + len(self.outStack)

    def peek(self):
        if not self.outStack:
            self._transfer()
        if self.outStack:
            return self.outStack[-1]

    def __repr__(self):
        if not self.outStack:
            self._transfer()
        if self.outStack:
            return repr(self.outStack)


if __name__ == "__main__":
    queue = Queue()
    print(f"is empty Queue ?: {queue.isEmpty()}")

    for i in range(5):
        queue.enqueue(i)
        print(f"Queue: {queue}")

    print(f"Queue size: {queue.size()}")
    print(f"peek: {queue.peek()}")

    queue.dequeue()
    print(f"peek: {queue.peek()}")
    print(f"Queue: {queue}")





