# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array)

# N X M 크기의 2차원 리스트
# 특정한 크기를 가지는 2차원 리스트를 초기화할 때에는 반드시 리스트 컴프리헨션을 이용해야 한다
n = 3
m = 4
array = [[0]*m for _ in range(n)]
print(array)

# _는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 사용
