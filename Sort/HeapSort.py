"""
힙 정렬: 힙에 모든 값을 push 한 다음, 가장 작은 값을 꺼내는(pop) 방법으로 구현할 수 있다.
- 시간 복잡도:
    -> 힙의 삽입: O(1)
    -> 힙 순서 확인: O(lon n)
    -> 힙 순회: O(n)

"""

import heapq


def heapSort(sequence):
    heap = []
    sortedList = []

    # 힙에 저장
    for element in sequence:
        heapq.heappush(heap, element)

    # 가장 작은 값 부터 pop
    for index in range(len(heap)):
        sortedList.append(heapq.heappop(heap))

    return sortedList


if __name__ == "__main__":
    sequence = [5, 3, 2, 4]
    assert(heapSort(sequence) == sorted(sequence))