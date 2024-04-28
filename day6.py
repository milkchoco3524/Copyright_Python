# str = input("How old are you: ")
# print(str ,'years old', sep=' ')


# x = int(input('number : '))
# print(x)


# x = float(input('number : '))
# print(x)

# year = input("This year: ")
# year = eval(year)
# year = year + 1
# print("Next year:", year)

# i = 0
# result = 0
# while i < 5:
#     i += 1
#     print(f'{i} 번째 ',end=" ")
#     i -= 1
#     a = input("성적 입력 : ")
#     result += int(a)
#     i += 1

# print(f"합 : {result}")
# print(f"평균 : {result / 5}")

# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# for i in range(1, 10):
#     print(i)



# from re import A



# result = 0
# for a in range(1, 100): #1 ~ 100

#     result = result + a
#     print(f"{a} sum = {result}")

# print(result)


# result = 0
# for a in range(1,101):
#     result = result + a     # a를 더해주고
#     print(f'{a} :  sum = {result}')         # 그때의 a값을 출력
#     if result > 100:    # result가 100이 넘었을때
#         break

# print(result)




# index = 0
# s = "BlockDMask"
# for a in s:
#     print(a,end=' ')
#     if a == 'k':
#         break       # 'k'를 찾았으니 for문에서 나와랏!

#     index = index + 1

# print(index)        # 'k'가 첫번재로 존재하는 위치 출력


# student = [180, 170, 164, 199, 172, 177]
# for a in student:
#     if a <= 170:

#         continue    # 키가 170보다 크면 continue

#     print(a)




# result = 0
# for a in range(1,101):  #1 ~ 100
#     if a % 2 == 1:      #2로 나누었을 때 나머지가 1
#         result = result + a

# print(result)


# result = 0
# for a in range(1,101):  #1 ~ 100
#     if a % 2 == 0:      #2로 나누었을 때 나머지가 1

#         continue
#     result = result + a

# print(result)



# l = ['Alice', 'Bob', 'Charlie']

# for name in l:
#     if name == 'Bob':
#         print("Break!")
#         break
#     print(name)
# else:
#     print("!! Finish")


# sr = ['father', 'mother', 'brother']
# cnt = 0
# for s in sr:
#     print(s)
#     for c in s:
#         print(c,end=' ')
#         if c == 'r':
#             print(' ')
#             cnt += 1
# print(cnt)



# a = []  # 빈 리스트 생성

# for i in range(3):
#     line = []           # 안쪽 리스트로 사용할 빈 리스트 생성
#     for j in range(2):
#         line.append(j+i)    # 안족 리스트에 0 추가
#     a.append(line)          # 전체 리스트에 안쪽 리스트를 추가

# print(a)


# for i in range(10,0,-3):

#     print(i)


l = ['Alice', 'Bob', 'Charlie']

for name in l:
    print(name)


for i, name in enumerate(l,42):
    print(i, name)