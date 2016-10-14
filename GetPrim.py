# -*- coding: utf-8 -*-
#定义质数的函数
#计算从0开始第1000个质数
def getprim(n):
    p = 3
    x = 0
    while(x<n):
        result = True
        for i in range(2,p-1):
            if(p%i==0):
                result = False
        if result==True:
            x=x+1
            rst=p
        p+=2
    print(rst)
getprim(1000)