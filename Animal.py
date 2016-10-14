# coding=utf-8
__metalclass__=type
class Animal:
    name="未知"
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setName(self,value):
        self.name=value
print(Animal.name)
print(Animal.__dict__["name"])

animal = Animal("狗狗")
print(animal.name)
print(animal.__dict__["name"])
print(Animal.name)
print(Animal.__dict__["name"])
print(animal.__class__.name)
print(animal.__class__.__dict__["name"])