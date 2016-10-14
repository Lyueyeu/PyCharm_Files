#coding=utf-8
'''
data=[0,1,2,3,4]
data[0]='a'
print(data)
data[0] = 0
del data[4]
print(data)
del  data[2:]
print(data)
data[2:]=[4,5,6]
print(data)
'''
'''
print(1,2)
print(1)
'''
'''
print("% 10s" % "____")
print('''
#%(title)s
#%(body)s
'''%{"title":"标题","body":"内容"})
'''
'''
print({"title":"title","body":"body"})
print(dict(title="title",body="body"))
print(dict([("title","title"),("body","body")]))
dic={"title":"titles","body":"bodys"}
print(dic["title"])
del dic["title"]
print(dic)
'''
'''
x,y,z=1,2,3
print(x,y,z)
(x,y,z)=(1,2,3)
print(x,y,z)
(x,y,z)=[1,2,3]
print(x,y,z)
'''
'''
if(10>1):
    print("10>1")
else:
    print("impossible")
'''
'''
x=[1,2,3]
y=x
z=[1,2,3]
print(x==y)
print(x==z)
print(x is y)
print(x is z)
'''
'''
for x in range(1,10):
    print(x)
for key in {"x":"xxx"}:
    print(key)
for key,value in {"x":"xxx"}.items():
    print(key,value)
for x,y,z in [["a",1,"A"],["b",2,"B"]]:
    print(x,y,z)
'''

'''
for index,value in enumerate(range(0,10)):
    print(index,value)
for x,y in zip(range(1,10),range(1,10)):
    print(x,y)
'''
'''
from math import  sqrt
for item in range(99,1,-1):
    root = sqrt(item)
    if(root == int(root)):
        print(item)
        break
else:
    print("没有执行break语句")
'''
'''
if(1==1):
    pass
exec('print(x)',{"x":"abc"})
print(eval('x*2',{"x":5}))
'''
'''
def func():
    print("func")
func()
def func_with_renturn():

    return("func_with_renturn")
print(func_with_renturn())

def  func_with_muti_return():
    return ("func_with_muti_return","func_with_muti_erturn")
print(func_with_muti_return())

def func_with_parameters(x,y):
    print(x,y)
func_with_parameters(1,2)

def func_with_collection_rest_parameters(x,y,*rest):
    print(x,y)
    print(rest)
func_with_collection_rest_parameters(1,2,3,4,5)

def func_with_named_paramenters(x,y,z):
    print(x,y,z)
func_with_named_paramenters(z=1,y=2,x=3)

def func_with_default_value_paraments(x,y,z=3):
    print(x,y,z)
func_with_default_value_paraments(y=2,x=1)

def func_with_collection_rest_named_paramenters(*args,**named_args):
    print(args)
    print(named_args)
func_with_collection_rest_named_paramenters(1,2,3,x=4,y=5,z=6)
func_with_collection_rest_named_paramenters([1,2,3],{"x":4,"y":4,"z":6})
func_with_collection_rest_named_paramenters(*[1,2,3],**{"x":4,"y":4,"z":6})
'''
'''
def func(x):
    def inner_func(y):
        print(x+y)
    return inner_func
inner_func=func(10)
inner_func(1)
inner_func(2)
'''
'''
if(2>1):
    x=1
print(x)
'''
'''
x=1
print(vars()["x"])#使用var函数可以访问当前作用域包含的变量
'''
'''
x=1
def func():
    print(globals()["x"])    #
func()
'''
'''
def func():
    x=2
    print(locals()["x"])#使用locals访问局部作用域
func()
'''
'''
x=1
def func():
    y=2
    print(x,y)  #访问规则为，函数执行时开启一个新的作用域，先访问当前的作用域，如果没有就访问函数定义时的作用域，递归直到全局作用域
func()
'''
'''
x=1
def func():
    x=2
    y=2
    print(x,y)  #变量赋值访问的始终为当前作用域
func()
print(x)
'''
'''
x=1
def func():
    global x
    x=2
    y=2
    print(x,y)  #局部变量会覆盖隐藏全局变量，想要访问全局变量可以采用global关键字或者globals()函数
func()
print(x)
'''

'''
def func(fn,arg):
    fn(arg)
func(print,"hello")
func(lambda arg : print(arg),"hello")
'''
'''
class HappyException(Exception):
    pass
try:
    raise HappyException
except:
    print("HappyException")
try:
    raise HappyException()
except:
    print("HappyException")
try:
    raise HappyException
except(HappyException,TypeError):
    print("HappyException")
'''

#L=['Michael','Sarah','Tracy','Bob','Jack']
#print([L[0],L[1],L[2]])
'''
r = []
n = 4
for i in range(n):
    r.append(L[i])
print(r)
'''
#print(L[-2:])


'''
L=list(range(100))
print(L)
'''

