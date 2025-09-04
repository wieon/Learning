# 输入某年某月某日，判断这一天是这一年的第几天

import datetime

year, month, day = map(int, input().split('-'))
yuandan = datetime.datetime(year, 1, 1)
now = datetime.datetime(year, month, day)
print((now-yuandan).days+1)