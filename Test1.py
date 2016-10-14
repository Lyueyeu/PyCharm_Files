import random
class Random(object):
    def get_String(length):
        data = []*length
        len = length
        while(len>0):
            data.append(random.randint(0, 10))
            len -= 1
        data1 = ''.join(map(str, data))    #获得数组后内容为数字，需要先转化为字符类型，才能重新拼接起来
        return data1
if __name__ == '__main__':
    Batch_No = Random.get_String(10)
    print(Batch_No)