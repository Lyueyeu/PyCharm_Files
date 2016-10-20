class Student(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0~100')
        self.__score = value
s = Student()
s.score = 60
print(s.score)
s.score = 999
print(s.score)