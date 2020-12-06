# Heap
#### 힙이란 ?
- 이진트리를 기반으로 만들어짐
- 리스트에서 가장 작거나(큰) 요소에 접근할 때 유용
- 시간 복잡도
    - 가장 작은(큰) 요소에 접근: O(1)
    - 조회, 추가, 수정: O(log n) 

#### 파이썬 Heapq 모듈
- import heapq 후 사용 가능
- heapq.heapify(): O(n) 으로 리스트를 힙으로 반환 가능
- heapq.heappush(heap, item): 힙에 항모 삽입
- heapq.heappop(heap): 힙에서 가장 작은 항목 제거 
- heapq.heqppushpop(heap, item): 새 항목을 힙에 추가 후, 가장 작은 항목 제거
- heapq.heapreplace(heap, item): 가장 작은 항목 제거 후, 새 항목 추가
- heapq.merge(*iterables): 여러 개의 정렬된 객체 병합 후 하나의 정렬된 객체 반환
- heappop() 메소드를 사용하는 것 보다 한번에 heappushpop(), heapreplace()를 사용하는게 효과적
