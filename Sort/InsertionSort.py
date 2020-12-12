"""
삽입 정렬: 배열 맨 처음 정렬된 부분에, 정렬되지 않은 다음 항목을 반복적으로 삽입하는 방식
- 데이터 크기가 작고, 리스트가 이미 정렬되어 있으면 병합 정렬이나 퀵 정렬 보다 성능 좋음
- 즉, 미리 정렬된 리스트에 새 항목을 추가할 때 좋다.
- 시간 복잡도: min -> O(n), max -> O(n^2)

example
- [11, 3, 28, 42, 9, 4]
  -----------------------------------
  -> Step1: 11 / 3 / 28 / 42 / 9 / 4
  -----------------------------------
  -> Step2: 3 / 11 / 28 / 42 / 9 / 4
  -----------------------------------
  -> Step3: 3 / 11 / 28 / 42 / 9 / 4
  -----------------------------------
  -> Step4: 3 / 9 / 11 / 28 / 42 / 4
  -----------------------------------
  -> Step5: 3 / 4 / 9 / 11 / 28 / 42

"""

def insertionSort(sequence):
    length = len(sequence)

    for lastIndex in range(1, length):
        for searchedIndex in range(lastIndex, 0, -1):
            if sequence[searchedIndex-1] > sequence[searchedIndex]:
                sequence[searchedIndex-1] = sequence[searchedIndex]
                sequence[searchedIndex] = sequence[searchedIndex-1]

    return sequence

if __name__ == "__main__":
    sequence = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    assert (insertionSort(sequence) == sorted(sequence))