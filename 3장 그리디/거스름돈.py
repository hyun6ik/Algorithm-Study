# 내가 생각했던 코드
# n = 1260
#
# five_hundred_won_number = n // 500
# n = n - (500 * five_hundred_won_number)
# one_hundred_won_number = n // 100
# n = n - (100 * one_hundred_won_number)
# fifty_won_number = n // 50
# n = n - (50 * fifty_won_number)
# ten_won_number = n // 10
# count = five_hundred_won_number + one_hundred_won_number + fifty_won_number + ten_won_number
#
# print("거스름kkkkkk돈 개수는 500원 {0}개, 100원 {1}개, 50원 {2}개, 10원 {3}개로 총 {4}개 입니다".format(
#     five_hundred_won_number, one_hundred_won_number, fifty_won_number, ten_won_number, count
# ))

# n = 1260
# count = 0
#
# coin_list = [500, 100, 50, 10]
#
# for coin in coin_list:
#     count += n // coin
#     n %= coin
#
# print(count)
