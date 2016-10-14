class TestClass:
    def method(self):
        print("测试方法")
test = TestClass()
print(TestClass.method)
print(test.method)
TestClass.method(test)
test.method()