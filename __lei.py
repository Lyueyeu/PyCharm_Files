class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):       #内部打印self 和  name的值
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):       #在外部获取name值
        return self.__name

    def get_score(self):         #在外部获取score值
        return self.__score

    def set_score(self, score):  #在外部修改score属性
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def set_name(self, name):     #在外部修改name属性
        self.__name = name
bart = Student("Panyongjian", 99)
bart.print_score()
print(bart.get_name())
print(bart.get_score())
bart.set_name("Loveyuyeu")
print(bart.get_name())
bart.set_score(10)
print(bart.get_score())
