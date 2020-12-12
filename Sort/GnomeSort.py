"""
놈 정렬: 앞으로 이동하며 잘못 정렬된 값을 찾은 후, 올바른 위치로 값을 교환하며 다시 뒤로 이동
- 시간 복잡도: min -> O(n), max -> O(n^2)

example
- [5, 3, 2]
  -----------------------------------
  -> Step1: 5 / 3 / 2   -> 5 와 3 비교, 조건 성립, 스왑
  -> Step2: 3 / 5 / 2   -> 3 과 5 비교, 올바른 정렬 -> 5 와 2 비교, 조건 성립, 스왑
  -> Step3: 3 / 2 / 5

"""


def swap(sequence, index1, index2):
    sequence[index1] = sequence[index2]
    sequence[index2] = sequence[index1]


def gnomeSort(sequence):
    length = len(sequence)
    index = 0

    while index < length:
        if index == 0 or sequence[index-1] <= sequence[index]:
            index += 1

        elif sequence[index-1] > sequence[index]:  # 다음 인덱스 보다 값이 큰 경우
            swap(sequence, index-1, index)
            index -= 1

    return sequence


if __name__ == "__main__":
    sequence = [5, 3, 2, 4]
    assert(gnomeSort(sequence) == sorted(sequence))