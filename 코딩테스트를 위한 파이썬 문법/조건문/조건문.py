score = 85

# if score >= 90:
#     print("A")
# elif score >=80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")
#

# if score >= 80:
#     pass
# else:
#     print("성적이 80점 미만입니다")
#
# print("프로그램 종료")

# if score >= 80: result = "Success"
# else: result = "Fail"
# print(result)

result = "Success" if score >= 80 else "Fail"
print(result)

a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]

print(result)