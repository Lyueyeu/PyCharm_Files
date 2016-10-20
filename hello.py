from Type import Hello
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls, name, bases,attrs)
class Mylist(list):
    __metaclass__ = ListMetaClass