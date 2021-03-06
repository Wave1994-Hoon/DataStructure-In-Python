"""
거품 정렬: 인접한 두 항목을 비교하는 정렬 방식
- 시간 복잡도: O(n^2)

example
- [11, 3, 28, 42, 9, 4]
  -----------------------------------
  -> Step1: 11 / 3 / 28 / 43 / 9 / 4
  -----------------------------------
  -> Step2: 3 / 11 / 28 / 9 / 4 / 43
  -----------------------------------
  -> Step3: 3 / 11 / 9 / 4 / 28 / 43
  -----------------------------------
  -> Step4: 3 / 9 / 4 / 11 / 28 / 43
  -----------------------------------
  -> Step5: 3 / 4 / 9 / 11 / 28 / 43
  -----------------------------------
"""


def swap(sequence, index1, index2):
    sequence[index1] = sequence[index2]
    sequence[index2] = sequence[index1]


def bubbleSort(sequence):
    length = len(sequence)

    for number in range(length-1, 0, -1):
        for index in range(number):
            if sequence[index] > sequence[index + 1]:
                swap(sequence, index, index + 1)

    return sequence

if __name__ == "__main__":
    sequence = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    assert(bubbleSort(sequence) == sorted(sequence))