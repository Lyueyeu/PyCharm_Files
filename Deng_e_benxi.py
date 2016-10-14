# 等额本息计算器
#计算每月偿还的本金和利息,总额
def getPerMonthPrincipalInterest(Invest, yearRate, totalMonth):
    monthRate = float(yearRate) / float(totalMonth)
    global MonthPay
    MonthPay = float(Invest) * (monthRate * (1 + monthRate) ** float(totalMonth)) / \
            ((1 + monthRate) ** float(totalMonth) - 1)
    return round(MonthPay, 2)

#计算每月偿还利息
def getPerMonthInterest(Invest, yearRate, totalMonth, NowMonth):
    monthRate = float(yearRate) / float(totalMonth)
    multiply = float(Invest) * monthRate
    sub = ((1 + monthRate) ** float(totalMonth)) - ((1 + monthRate) ** (float(NowMonth) - 1))
    monthInterest = (multiply * sub) / ((1 + monthRate) ** float(totalMonth) - 1)
    return round(monthInterest, 2)

#计算每月应还的本金
def getPerMonthPrincipal(Invest, yearRate, totalMonth, nowMonth):
    monthRate = float(yearRate) / float(totalMonth)
    global MonthPrincipal
    MonthPrincipal = float(Invest) * monthRate * ((1 + monthRate) ** (float(nowMonth) - 1)) / (
        (1 + monthRate) ** float(totalMonth) - 1)
    return round(MonthPrincipal, 2)

#计算总应还本金和利息
def getPrincipalInterestCount(Invest, yearRate, totalMonth):
    monthRate = float(yearRate) / float(totalMonth)
    perMonthInterest = float(Invest) * (monthRate * ((1 + monthRate) ** float(totalMonth))) / \
                       ((1 + monthRate) ** float(totalMonth) - 1)

    count = perMonthInterest * totalMonth
    return round(count, 2)

# 计算应还的总利息
def  getInterestCount(Invest, yearRate,  totalMonth):
    global InterestCount
    InterestCount = getPrincipalInterestCount(Invest, yearRate, totalMonth) - Invest
    return InterestCount
    
if __name__ == '__main__':
     MonthPay = getPerMonthPrincipalInterest(2000, 0.13, 12)
     print("每月应还本金和利息：%.2f" % MonthPay)
     MonthPrincipal = getPerMonthPrincipal(2000, 0.13, 12, 2)
     print("每月应还本金：%.2f" % MonthPrincipal)
     MonthInterest = getPerMonthInterest(2000, 0.13, 12, 2)
     print("每月应还利息：%.2f" % MonthInterest)
     InterestCount = getInterestCount(2000, 0.13, 12)
     print("应还利息总额：%.2f" % InterestCount)
     PrincipalInterestCount = getPrincipalInterestCount(2000, 0.13, 12)
     print("应还本金和利息总额：%.2f" % PrincipalInterestCount)


