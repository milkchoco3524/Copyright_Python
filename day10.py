# def func1():
#     print("BlockDMask")

# # 함수 호출
# func1()
# func1()
# func1()

# for i in range(3):
#     func1()

# def func2(a, b):
#     print(f'{a} 곱하기 {b} = {a * b}')

# # 함수 호출
# func2(1, 2)
# func2(1, 3)
# func2(2, 4)

# def func3():
#     return "abcdefg"

# # 함수 호출

# a = func3()
# print(a , "GG", sep=" " )

# def func4(a, b):
#     return a * b

# # 함수 호출
# a = input()
# c = func4(int(a), 9)
# print(c)


# for i in range(1, 10):
#     print(f'{2} x {i} = {2 * i}')
# for i in range(1, 10):
#     print(f'{3} x {i} = {3 * i}')

# print()
# print()
# print()

# def gugudan(num):
#     for i in range(1, 10):
#         print(f'{num} x {i} = {num * i}')
#     print()


# # 구구단 출력
# gugudan(2)

# gugudan(2)

# # 디폴트 파라미터 예제 1
# def func1(a, b=5, c=10):
#     return a + b + c

# print( func1(1, 2, 3) ) # 1 + 2 + 3
# print( func1(1, 2) ) # 1 + 2 + 10
# print( func1(1) ) # 1 + 5 + 10

# print()


# # 디폴트 파라미터 예제 2
# def func2(a=10, b=20):
#     return a + b

# print( func2(1, 2)) # 1 + 2
# print( func2 (1) ) # 1 + 20
# print( func2() ) # 10 + 20

# def func3(a = 10, b, c): # error
#     return a + b + c

# func3(1, 2)     # 1이 a이고 2가 b에 들어가는거겠지?
#                 # 뭘 원하는거야? error
# func3( , 1, 2)  # 뭐 이렇게 호출해야하나? error 헤헤헤헤헿

# def func6(*args):
#     a = 0
#     for i in args:
#         a = a + i
#     return a

# b = func6(1, 5)
# print(b)

# b = func6(1, 5)
# print(b)

# c = func6(2, 3, 4, 5)
# print(c)

# d = func6(1, 2, 3, 4, 5, 4, 3, 2, 1)
# print(d)

# e = func6()
# print(e)


# def test(*val):
#     for i in val:
#         print(i)

# test(1,'a','c',3)

# def sum_mul(choice, *val):
#     if choice == 'sum':
#         result = 0
#         for i in val:
#             result = result + i
#     elif choice == 'mul':
#         result = 1
#         for i in val:
#             result = result * i
#     print()
#     return result


# print (sum_mul('sum', 1,2,3,4,5))

# print (sum_mul('mul', 1,2,3,4,5))


# def comp (score=0):
#     if score == 0:
#         return 0
#     elif score > 50:
#         return 2
#     else:
#         return 1

# grade = comp(40)
# print ("Grade is ", grade, " for ", 40)

# grade = comp(80)
# print ("Grade is ", grade, " for ", 80)

# grade = comp()
# print ("Grade is ", grade, "for no score")


def report(name, age, score):
    print(name, score)

report(age=10, name="Kim", score=80)
report("Kim",10,80)