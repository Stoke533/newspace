# rows = int(input('Enter number of rows: '))
# k = 0
# for i in range(1, rows+1):
#     for space in range(1, (rows-i) +1):
#         print(end=' ')
#     while k != (2*i-1):
#         print("*", end='')
#         k += 1
#     k = 0
#     print()


# import re
# str = '经济舱 ¥360起公务/头等舱 ¥1250起不得改期|托运行李额20KG行程单经济舱1.8折82折接送机新客券免税店优惠礼包¥360选购展开查看所有产品(6666)'
# if '展开查看所有产品' in str:
#     pat = re.findall('选购展开查看所有产品(.*)', str)[0]
#     print(pat)
#     print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
#     dat = f'展开查看所有产品{pat}'
#     print(dat)
#     print('**********************')
#     str = str.replace(dat, '')
#     print(str)
#     print('------------------')
# else:
#     pass
# print(str)


# def outer(func):
#     def inner(*args, **kwargs):
#         print('before!')
#         res = func(*args, **kwargs)
#         print('after!')
#         return res
#     return inner
#
# @outer
# def yang(y):
#     print(y + 'jiayou!')
#
# yang('yang')



# class Singleton:
#     __instance = None
#
#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#
# s1 = Singleton()
# print(s1)
# s2 = Singleton()
# print(s2)
#
# print(s1 is s2)


# a = [1,2,3]
# c = a.join(a)
# print(c)