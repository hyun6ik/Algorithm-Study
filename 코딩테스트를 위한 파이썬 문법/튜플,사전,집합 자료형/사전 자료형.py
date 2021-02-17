data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print(data['사과'] +"을/를 데이터로 가지는 키가 존재합니다")

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])