# 如果你需要遍历一个数字序列，可以是使用python中内建的函数range()

# 如下面要遍历一个列表test_list
test_list = [1, 3, 4, 'Hongten', 3, 6, 23, 'hello', 2]
for i in range(len(test_list)):
    print(test_list[i], end=',')

print()
print('#####################################')

# 或者用range()函数生成一个列表
for i in range(5):
    print(i, end=',')

print()
print('#####################################')

# python中的内置函数range(10),其中参数'10'代表：从0到10的一个序列
# 即长度为10的一个序列
print('range(10)表示：', range(10))
listA = [i for i in range(10)]
print(listA)

print('#####################################')

# 当然，我们可以自定义我们需要的起始点和结束点
# 我们定义了一个从5开始的起始点，到100结束的结束点
print('range(5,100)表示：', range(5, 100))
listB = [i for i in range(5, 100)]
print(listB)

print('#####################################')

# 定义了这些后，我们还可以定义步长
# 下面我们定义一个从1开始到30结束，步长为3的列表
print('range(1,30,3)表示：', range(1, 30, 3))
listC = [i for i in range(1, 30, 3)]
print(listC)