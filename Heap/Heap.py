class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        for i in range(len(data), -1, -1):
            self.__maxHeapify__(i)

    def __repr__(self):
        return repr(self.data)

    def parent(self, i):
        if i & 1:
            return i >> 1
        else:
            return (i >> 1) - 1

    def leftChild(self, i):
        return (i << 1) + 1

    def rightChild(self, i):
        return (i << 1) + 2

    def __maxHeapify__(self, i):
        largest = i  # 현재 노드
        left = self.leftChild(i)
        right = self.rightChild(i)
        n = len(self.data)

        # 왼쪽 자삭
        largest = (left < n and self.data[left] > self.data[i]) and left or i

        # 오른쪽 자식
        largest = (right < n and self.data[right] > self.data[largest]) and right or largest

        # skip: 현재 노드 > 자식 노드  / Swap: 현재 노드 < 자식 노드
        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.__maxHeapify__(largest) # print(self.data)

    def extractMax(self):
        n = len(self.data)
        maxElement = self.data[0]

        # 첫 버쨰 노드에 마지막 노드 삽입
        self.data[0] = self.data[n-1]
        self.data = self.data[:n-1]
        self.__maxHeapify__(0)

        return maxElement

    def insert(self, item):
        i = len(self.data)
        self.data.append(item)

        while (i != 0) and item > self.data[self.parent(i)]:
            print(self.data)
            self.data[i] = self.data[self.parent(i)]
            i = self.parent(i)

        self.data[i] = item

if __name__ == "__main__":
    listExample = [3, 2, 5, 1, 7, 8, 2]
    heap = Heapify(listExample)

    assert(heap.extractMax() == 8)
    print("Success !!")


















