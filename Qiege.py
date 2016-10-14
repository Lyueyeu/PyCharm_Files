# -*- coding: utf-8 -*-
#split用于拆分字符串，join用于连接字符串
low_strs = 'abcd'
uper_strs = 'EFGH'
test_strA = 'hello_world'
test_strB = 'goodBoy'
test_strC = 'hello_for_our_world'
test_strD = 'hello_our_world'

#小写转大写
low_strs = low_strs.upper()
print("小写转大写：", low_strs)

#大写转小写
uper_strs = uper_strs.lower()
print("大写转小写：", uper_strs)

#只大写第一个字母
test_strB = test_strB[0].upper()+test_strB[1:]
print("大写第一个字母：", test_strB)

#去掉中间的_,也可以去掉其他字符
test_strA = ''.join(test_strA.split('_'))
print("去掉特定的字符：", test_strA)


# 去除'hello_for_our_world'中的'_',并且把从第一个'_'以后的单词首字母大写,oriStr--总字符，splitStr--要去除的字符
def get_str(oriStr, splitStr):
    str_list = oriStr.split(splitStr)
    if len(str_list) > 1:
        for index in range(1, len(str_list)):
            if str_list[index] != '':
                str_list[index] = str_list[index][0].upper() + str_list[index][1:]
            else:
                continue
        return ''.join(str_list)
    else:
        return oriStr


print('去除\'hello_for_our_world\'中的\'_\',并且把从第一个\'_\'以后的单词首字母大写:', get_str(test_strC, '_'))
print('去除\'hello__our_world_\'中的\'_\',并且把从第一个\'_\'以后的单词首字母大写:', get_str(test_strD, '_'))


str_list = test_strC.split('_')
print(str_list)

str_list = test_strD.split('_')
print(str_list)