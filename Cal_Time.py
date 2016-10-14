# -*- coding: utf-8 -*-
#获取今天和昨天的日期
#引入datetime模块
import datetime
#计算今天的时间
today = datetime.date.today()
#计算昨天的时间
yesterday = today - datetime.timedelta(days = 1)
#计算明天的时间
tomorrow = today + datetime.timedelta(days = 1)
#打印三个时间
print(today, yesterday, tomorrow)