# -*- coding: utf-8 -*-
import datetime
import time
import json
def Cal_Interest(Amount,Rate,Days):                # 计算利息
    interest=Amount*(Rate/365/100)*Days
    return interest

def Cal_Days(IntrStartDay,IntrEndDay):            # 计算计息天数
    date1 = time.strptime(IntrStartDay, "%Y-%m-%d")
    date2 = time.strptime(IntrEndDay, "%Y-%m-%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2],)
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    Days = (date2 - date1).days
    return Days


def Cal_Date(Date,num):                           #加天数，得到一个日期
    D1 = time.strptime(Date, "%Y-%m-%d")
    D2 = datetime.datetime(D1[0], D1[1], D1[2],)
    D3 = D2 + datetime.timedelta(num)
    return D3.strftime('%Y-%m-%d')   #转换成字符串


def Cal_Pay_type(Date_Due,Due_Date):
    Date_Due1 = time.strptime(Date_Due, "%Y-%m-%d")
    Due_Date1 = time.strptime(Due_Date, "%Y-%m-%d")
    date1 = datetime.datetime(Date_Due1[0], Date_Due1[1], Date_Due1[2], )
    date2 = datetime.datetime(Due_Date1[0], Due_Date1[1], Due_Date1[2])
    if (date1 - date2).days < 0:
        return "02"
    else:
        return "01"


if __name__ == '__main__':
    # 输入内容
    # Batch_No = input("批次号：")
    # Contract_No = input("合同号：")
    # IntrStartDay = input("放款日期：")
    # IntrEndDay = input("还款日期：")
    # Due_Date = input("到期日:")
    # Need_Principal = input("当次还款金额：")
    print("分别输入批次号、合同号、放款日期、还款日期、到期日、当次还款金额!!!")
    arr = [""] * 6
    i = 0
    while (i < 6):
        arr[i] = input()
        i += 1
    Days = Cal_Days(arr[2], arr[3])
    interest = round(Cal_Interest(int(arr[5]), 13, Days), 2)       #计算利息，并且保留两位小数
    # 转换成数组
    data = {}
    data["bank_Name"] = "中国农业银行"      #银行名称
    data["bank_No"] = "6228480348646882277"          #银行卡号
    data["batch_Count"] = 1                       #批次数量，这个可以忽略
    data["batch_No"] = arr[0]             #批次号
    data["city"] = "嘉兴"                 #城市
    data["contract_No"] = arr[1]               #合同号
    data["credit_Amount"] = 100000            #借款总额
    data["due_Date"] = arr[4]                    #到期日
    data["interest_Fee"] = "0.047"                  #利息费率
    data["Pay_Date"] = Cal_Date(arr[3], 1)          #客户支付日期
    data["name"] = "何一一"                            #这个可以随便填，客户名称
    data["need_Amount"] = float(arr[5]) + interest     #当次还款总额
    data["need_Interest"] = interest            #当次还款利息
    data["need_Principal"] = arr[5]     #当次还款本金
    data["pay_Status"] = "k"                    #当次还款状态，这个是针对客户还给达飞的情况，我们不需要考虑
    data["pay_Type"] = Cal_Pay_type(arr[3], arr[4])                   #01为现行，02为提前还款
    data["release_Date"] = arr[2]         #放款日期
    data["Pay_Num"] = "0"                       #已还款次数
    data["Pay_Amount"] = "0"                    #已还款总额
    data["last_Due_Date"] = arr[3]          #上一次还款日期
    data["Date_Due"] = arr[3]               #达飞还PP日期
    data["Need_Interest_Parner"] = interest     #达飞应付PP利息

    # class CJsonEncoder(json.JSONEncoder):
    #     def default(self, obj):
    #         if isinstance(obj, datetime):
    #             return obj.strftime('%Y-%m-%d %H:%M:%S')
    #         elif isinstance(obj, datetime.date):
    #             return obj.strftime('%Y-%m-%d')
    #         else:
    #             return json.JSONEncoder.default(self, obj)


    jsonStr = json.dumps(data,ensure_ascii=False)          # 转换为json格式
    print("["+jsonStr+"]")


