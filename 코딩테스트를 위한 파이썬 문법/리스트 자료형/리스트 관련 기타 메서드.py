a = [1,4,3]
print("기본 리스트: ", a)

a.append(2)
print("삽입 : ", a)

a.sort()
print("오름차순 정렬 :", a)

a.sort(reverse=True)
print("내림차순 정렬 :", a)

a.reverse()
print("원소 뒤집기 : ", a)

a.insert(2,3)
print("인덱스 2에 3추가", a)

print("값이 3인데이터 개수 :", a.count(3))

a.remove(1)
print("값이 1인 데이터 삭제 :", a)

# append의 시간 복잡도 = O(1)
# insert, remove 시간 복잡도 = O(N) : 원소를 추가,삭제한 후 다시 리스트의 원소 위치를 조정해야하기 때문

# 특정한 값의 원소를 모두 제거
a = [1,2,3,4,5,5,5]
remove_set = {3,5}
print(a)

result = [i for i in a if i not in remove_set]
print(result)