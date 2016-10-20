import json
import random
import time
class Random(object):
    def get_String(length):
        data = [] * length
        len = length
        while (len > 0):
            data.append(random.randint(0, 10))
            len -= 1
        data1 = ''.join(map(str, data))  # 获得数组后内容为数字，需要先转化为字符类型，才能重新拼接起来
        return data1

class Time_String(object):
    def getTimeString(self):
        curTime = time.strftime("%Y%m%d", time.localtime(time.time()))
        return curTime

if __name__ == '__main__':
    Batch_No = Time_String().getTimeString() + Random.get_String(3)
    Release_Date = input("放款日期：")
    Due_Date = input("到期日：")
    num = input("该批次有多少个合同：")
    arr = [""]*int(num)
    i = 0
    while (i < int(num)):
        arr[i] = Time_String().getTimeString() + Random.get_String(6)
        i += 1
    data = {}
    sum = 0
    print("[")
    for con in arr:
        data['Batch_No'] = Batch_No
        data["Batch_Count"] = num
        data["Contract_No"] = con
        data["Person_Name"] = "庄一一"
        data["Ident"] = "441121199409044101"
        data["Release_Date"] = Release_Date
        data["Credit_Amount"] = Random.get_String(1)+"000"
        data["Due_Date"] = Due_Date
        data["Mobile"] = "13357665332"
        data["Ident_Exp"] = "2023-03-27"
        data["Ident_Auth"] = "玉环县公安局"
        data["Sex"] = "女"
        data["Company"] = "富甲汽配制造厂"
        data["Bank_Name"] = "中国农业银行"
        data["Account_No"] = "6228480368025709776"
        data["Address"] = "浙江省玉环县新塘路131号"
        data["Income"] = "10000"
        data["Marital_Status"] = "已婚"
        data["Education"] = "职高/中专/技术学校"
        data["Bank_Account_No"] = "庄一一"
        data["Repayment_Type"] = "04"
        data["Attachment_Url_Path"] = "201607P2P_PPM_SC_CYCLECREDIT.1.DAFYSEAL.0.PDF_Cert.pdf"
        data["Interest_Fee"] = "0.0047"
        data["Max_Amount"] = "10000"
        data["Active_Amount"] = "10000"
        data["Available_Amount"] = "10000"
        credits = ''.join(data["Credit_Amount"])
        sum = int(credits)+ sum
        jsonStr = json.dumps(data, ensure_ascii=False, sort_keys=True)
        print(jsonStr)
    print("]")
    data1 = {}
    data1["batchNo"] = Batch_No
    data1["totalCount"] = num
    data1["totalAmount"] = sum
    jsonStr1 = json.dumps(data1, ensure_ascii=False, sort_keys=True)
    print("["+jsonStr1+"]")



