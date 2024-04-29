# a = 'I love Python'
# print( len(a) )


# b = 'abcd'
# print( len(b) )


# name = 'BlockDMask'
# phone = '010 xxxx xxxx'
# address = 'korea'
# print(len(name))
# print(len(phone))
# print(len(address))


# a = [1, 2, 3]
# print(max(a))

# b = 'bBlockDMask'
# print(max(b))

# c = 1
# # print(min(c))

# d = (6, 5, 4, 2)
# print(max(d))

# e = [3,4,5, 'a','b','c']
# # print(min(e))


# a = [1,2,3]
# b = [1,2,4]
# print(min(a,b))

# c = 'BBB'
# d = 'BBa'
# print(min(c,d))


# g = [2,3,4]
# h = [2,2,2,2,2]
# i = [9,8,7,6,5]
# j = [1]
# k = [0]
# print(min(g,h,i,j,k))


# myString = "everdevel"
# print(myString.count('ev'))


# a = 'BlockDMask'

# print("#1 a.count('k')")
# print(a.count('k'))
# print('#2 a.count("DM")')
# print(a.count('DM'))
# print("#3 a[2] + '~' + a[4]")
# print(a[2] + ' ~ ' + a[4])
# print("#4 a.count('k',2, 3)")
# print(a.count('k', 2, 3))
# print("#5 a.count('k', 2, 4)")
# print(a.count('k', 2, 4))
# print("#6 a.count('k', 2, 5)")
# print(a.count('k', 2, 6))


# str = ".BlockDMascleark Blog"
# print(f"str : {str}\n")

# # find 예제1
# print("1. str.rfind('찾을 문자')")
# result1 = str.rfind('.',0,5)

# # 문자가 있는 경우
# result2 = str.find('z')

# 문자가 없는 경우
# print(f"str.rfind('.') : {result1}")
# print(f"str.find('z') : {result2}")


# result3 = str.find('ask')
# print(f"str.find('ask') : {result3}")


# result4 = str.find('kkk')
# # 문자열이 없는 경우
# print(f"str.find('kkk') : {result4}")
# print()


# print("2. str.find('찾을 문자', 시작 index)")
# result5 = str.find('o')
# result6 = str.find('o',5)
# print(f"str.find('o') : {result5}")
# print(f"str[5] : {str[5]}")
# print(f"str.find('o',5) : {result6}")
# print()



# str = 'Hello world, Python!'

# print(len(str))

# if str.startswith("Hello"):
#     print('It starts with Hello')

# if str.endswith('Python'):
#     print('It does not start with Hello')


# print(str.startswith("Hello",1))
# print(str.endswith('Python!',1,20))



# str = 'this is string example....wow!!!'

# print(len(str))
# suffix = "wow!!!"
# print(str.endswith(suffix))
# print(str.endswith(suffix,20))

# suffix = "is"
# print(str.endswith(suffix, 2, 4))
# print(str.endswith(suffix, 2, 7))



# a = [123, 421, 212, 11, 24, 102, 29, 92, 10]
# print(a.index(212))


# nums_list = [1,2,3,3,3,5,6,8,9]
# nums_tuple = (1,2,3,3,3,5,6,8,9)
# nums_set = {1,2,3,5,6,8,9}

# print(nums_list.index(2))   # 1
# print(nums_list.index(3))   # 2
# # -> 찾고자 하는 데이터가 여러 개 존재할 경우, 가장 작은 위치 값 반환

# print(nums_tuple.index(2))  # 1
# print(nums_tuple.index(3))  # 2

# # print(nums_set.index(2))  # 1
# # print(nums_set.index(3))  # 2



text = 'Welcome to Codetorial'

pos_Code_last = text.rindex('Code')
print(pos_Code_last)

pos_code_last = text.rfind('code')
print(pos_code_last)

pos_code_last = text.rindex('code')
print(pos_code_last)