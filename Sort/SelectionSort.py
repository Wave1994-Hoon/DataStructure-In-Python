"""
선택 정렬: 먼저 리스트에서 가장 작거나 큰 항목을 찾아서 첫 번째 항목과 위치를 교환, 이 행위를 반복
- 시간 복잡도: O(n^2) --> 리스트가 이미 정렬되어 있어도(안정적이지도 않음)

example
- [11, 3, 28, 42, 9, 4]
  -----------------------------------
  -> Step1: 11 / 3 / 28 / 42 / 9 / 4
  -----------------------------------
  -> Step2: 3 / 11 / 28 / 42 / 9 / 4
  -----------------------------------
  -> Step3: 3 / 4 / 28 / 42 / 9 / 11
  -----------------------------------
  -> Step4: 3 / 4 / 9 / 42 / 28 / 11
  -----------------------------------
  -> Step5: 3 / 4 / 9 / 11 / 28 / 42

"""


def swap(sequence, index1, index2):
    sequence[index1] = sequence[index2]
    sequence[index2] = sequence[index1]


def selectionSort(sequence):
    length = len(sequence)

    for startIndex in range(length - 1):
        minimumIndex = 0
        for searchedIndex in range(startIndex+1, length):
            if sequence[minimumIndex] > sequence[searchedIndex]:
                minimumIndex = searchedIndex

        swap(sequence, startIndex, minimumIndex)

    return sequence


if __name__ == "__main__":
    sequence = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    assert (selectionSort(sequence) == sorted(sequence))