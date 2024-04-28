# # name = 'test'
# # if name == 'test':
# #     print("이름이 맞습니다.")
# # else:
# #     print("이름이 틀립니다.")


# pocket = 1000
# if pocket == 1000:
#     print("복권 구매")
# elif pocket == 500:
#     print("껌 구매")
# else:
#     print("집")


# a = "사과"
# b = "바나나"
# c = "치즈"

# if a =="사과" or b == "안바나나":
#     print("사과 이거나 바나나 입니다.")
# if a == '사과' or b == '바나나':
#     print("사과이고 바나나 입니다.")
# if not c =="사과":
#     print("사과가 아니어야 합니다.")


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# if 1 in a :
#     print("1 is in a")

# if 10 in a :
#     print("10 is in a")


# p_class = 'B'
# sel_amount = 7900

# if p_class == 'A':
#     sel_amount *= 0.7
#     print(f'판매가는 {sel_amount}원입니다')
# elif p_class == 'B':
#     sel_amount *= 0.85
#     print(f'판매가는 {sel_amount}원입니다')
#     print('판매가는 %f원입니다' % sel_amount)

# X = 2

# if (X%2 == 0):
#     print("Even number")

# else:
#     print("Odd Number")

X = 12

# if X < 10:
#     print("X는 10보다 작아!")
#     if X%2 == 0:
#         print('X는 짝수야!')
#     else:
#         print('X는 홀수야!')
# else:
#     print('X는 10보다 커!')
#     if X%2 == 0:
#         print('X는 짝수야!')
#     else:
#         print('X는 홀수야!')

# if X<10 and X%2 == 0:
#     print('X는 10보다 작으면서 짝수야!')
# if X<10 and not X%2 == 0:
#     print('X는 10보다 작으면서 홀수야!')
# if not X<10 and X%2 == 0:
#     print('X는 10보다 크면서 짝수야!')
# if not X<10 and not X%2 == 0:
#     print('X는 10보다 크면서 홀수야!')

# treeHit = 0

# while treeHit < 10:
#     treeHit = treeHit +1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee -1
#     break
#     print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

# i = 0
# result1 = 0
# while i < 100:
#     i = i + 1
#     if i % 2 ==0:
#         print('1번 방법 : {0} {1}'.format(i, result1))
#         result1 = result1 + i

# print('1번 방법 : {0}'.format(result1))



# i = 0
# result1 = 0
# while i < 100:
#     i = i + 1
#     #if i % 2 ==0:
#     print('1번 방법 : {0} {1}'.format(i, result1))
#     result1 = result1 + i

# print('1번 방법 : {0}'.format(result1))

# j = 0
# result2 = 0
# while True:
#     if j > 100:
#         break

#     j = j + 1
#     if j % 2 == 0:
#         result2 =  result2 + j

# print('2번 방법 (break) : {0}'.format(result2))

k = 0
result3 = 0
while k < 100:
    k = k + 1
    if k % 2 != 0:
        continue

    result3 = result3 + k

print('3번 방법 (continue) : {0}'.format(result3))