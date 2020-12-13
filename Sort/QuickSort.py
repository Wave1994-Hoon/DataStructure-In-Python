"""
퀵 정렬: 피벗 앞에는 피벗보다 자근 값이 오고, 피벗 뒤에는 피버보다 큰 값이 오도록 피벗을 기준으로 리스트를 둘로 나눔
- 피벗이란?
    ->  리스트에서 기준이 되는 하나의 요소
- 피벗을 중앙 값으로 선택하는게 무난함


example
- [5, 3, 2, 4, 7]


                        before: [] / pivot: 2 / after: [5, 3, 4, 7]



                  []                     [2]              before: [3] / pivot: 4 / after: [5, 7]



        []                []                    [3]                 [4]        before: [5] / pivot: 7 / after: []

"""


def quickSortCache(sequence):
    length = len(sequence)

    if length < 2:
        return sequence

    pivotIndex = length // 2
    pivot = sequence[pivotIndex]

    after, before = [], []

    for index, element in enumerate(sequence):
        if index == pivotIndex:
            continue

        if element <= pivot:
            before.append(element)

        if element > pivot:
            after.append(element)

    return quickSortCache(before) + [pivot] + quickSortCache(after)


if __name__ == "__main__":
    sequence = [5, 3, 2, 4, 7]
    assert (quickSortCache(sequence) == sorted(sequence))
