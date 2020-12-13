"""
병합 정렬: 리스트를 반으로 나누어 정렬되지 않은 릿트를 만든다.
         -> 정렬되지 않은 두 리스트의 크기가 1이 될 때까지, 계속 리스트를 반으로 나누어 병합 정렬 알고리즘을 호출하여 리스트를 정렬하고 병합한다.
         -> 안정적인 정렬 알고리즘이며, 대규모 데이터에 대해서도 속도가 빠르다.
         -> 하지만 배열의 경우 제자리에서 정렬되지 않기 때문에 다른 알고리즘 보다 훨씬 더 많은 메모리가 필요
         -> 공간 복잡도: 배열 -> O(n), 연결리스트 -> O(log n)
         -> 시간 복잡도: O(n log n)
"""


def mergeSort(sequence):
    length = len(sequence)

    if length < 2:
        return sequence

    middle = length // 2
    left, right = sequence[:middle], sequence[middle:]

    if len(left) > 1:
        left = mergeSort(left)

    if len(right) > 1:
        right = mergeSort(right)

    sortedList = []

    while left and right:
        if left[-1] >= right[-1]:
            sortedList.append(left.pop())
        else:
            sortedList.append(right.pop())

    sortedList.reverse()

    return (left or right) + sortedList


if __name__ == "__main__":
    sequence = [5, 3, 2, 4]
    assert(mergeSort(sequence) == sorted(sequence))