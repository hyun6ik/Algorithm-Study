import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

def maxheapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result = maxheapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 힙 = 트리구조 정렬
# 최대힙 = 부모노드가 자식노드보다 무조건 큰놈
# 최소힙 = 부모노드가 자식노드보다 무조건 작은놈(파이썬에서는 기본)
# 10 -> 20 -> 30  = 최소힙
# 10 -> 30 -> 20 = 최소힙
# 힙 규칙 : 힙 순서 속성(부모가 무조건 작아야함)
# 힙 삭제 : 루트 먼저 삭제

#  스택 = LIFO 가장 먼저 들온 놈이 가장 나중에 나온다

