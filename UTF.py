# -*- coding: utf-8 -*-
#参数前加一个星号，表明将所有的值放在同一个元组中，该参数的返回值是一个元组。
#参数前加两个星号，表明将所有的值放在同一个字典中，该参数的返回值是一个字典。
中国 = 'china'
print(中国)
def print_param(x, y, z = 3,*pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)
print_param(3, 4, 5, 6, 7, 8, m=1, n=2)

