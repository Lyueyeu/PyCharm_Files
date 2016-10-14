class Base1:
    pass
class Base2:
    pass
class Child(Base2,Base1):
    pass
child = Child()
print(isinstance(child,Child))
print(isinstance(child,Base2))
print(isinstance(child,Base1))