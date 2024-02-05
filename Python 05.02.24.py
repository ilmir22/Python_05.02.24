# class Fib:
#     def __init__(self, nn):  
#         print ("_init_")
#         self._n = nn
#         self._i = 0
#         self._p1 = self._p2 = 1
#     def __iter__(self):
#         print("_iter_")
#         return self
    
#     def __next__(self):
#         print("_self_")
#         self._i += 1
#         if self._i > self._n:
#             raise StopIteration
#         if self._i in [1, 2]:
#             return 1
#         ret = self._p1 + self._p2
#         self._p1, self._p2 = self._p2, ret
#         return ret
# for i in Fib(10):
#     print(i)
#-------------------------------------------------
# def fun(n):
#     for i in range(n):
#         yield i
    

# for v in(fun(5)):
#     print(v)
#-----------------------------------------------------

# def powersOf2 (n):
#     pow = 1
#     for i in range(n):
#         yield pow
#         pow *= 2
# for v in powersOf2(8):
#     print(v)
#----------------------------------------------------------

# def Fib(n):
#     p = pp = 1
#     for i in range(n):
#         if i in [0, 1]:
#             yield 1
#         else:
#             n = p+pp
#             pp, p = p, n
#             yield n
# fibs = list(Fib(10))
# print(fibs) 
#------------------------------
# two = lambda :2
# sqr = lambda x : x * x
# pwr = lambda x, y: x ** y

# for a in range (-2, 3):
#     print (sqr(a), end="")
#     print (pwr(a, two()))

# /////////////////////////////////////////
# list_num = [1, 2, 3, 4, 5]
# my_list = list(map(lambda x: x*2, list_num))

# print(list_num)
# print(my_list)