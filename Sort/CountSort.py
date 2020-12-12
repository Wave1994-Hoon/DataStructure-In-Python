"""
카운트 정렬: 숫자의 발생 횟수를 계산하는 누적 카운트 방식 사용, 누적 카운트를 갱신해서 순서대로 숫자를 직접 배치
- 작은 범위의 정수를 정렬할 때, 유용
- 숫자의 간격이 크거나 로그 선형 제한에 걸리면 비효율적
- 시간 복잡도: O(n+k),  k = 리스트 중 가장 큰 수

example
- sequence = [3, 5, 2, 6, 8, 1, 0]

Step1: Make dictionary
------------------------------------------------------------
{3: [3]})
{3: [3], 5: [5]})
{3: [3], 5: [5], 2: [2]})
{3: [3], 5: [5], 2: [2], 6: [6]})
{3: [3], 5: [5], 2: [2], 6: [6], 8: [8]})
{3: [3], 5: [5], 2: [2], 6: [6], 8: [8], 1: [1]})
{3: [3], 5: [5], 2: [2], 6: [6], 8: [8], 1: [1], 0: [0]})
------------------------------------------------------------

Step2: Add key's value to list in sequence
------------------------------------------------------------
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3, 5]
[0, 1, 2, 3, 5, 6]
[0, 1, 2, 3, 5, 6]
[0, 1, 2, 3, 5, 6, 8]
------------------------------------------------------------
"""

from collections import defaultdict


def countSort(sequence):
    result = []
    dictionary = defaultdict(list)

    for listElement in sequence:
        dictionary[listElement].append(listElement)

    for dictionaryKey in range(min(dictionary), max(dictionary)+1):
        result.extend(dictionary[dictionaryKey])

    return result


if __name__ == "__main__":
    sequence = [3, 5, 2, 6, 8, 1, 0]

    # sequence = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    assert (countSort(sequence) == sorted(sequence))