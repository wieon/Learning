import datetime
date = input().split('/')
date_int = [int(x) for x in date]
date_customed = datetime.date(date_int[0],date_int[1],date_int[2])  # 创建一个自定义日期对象
yday = date_customed.timetuple().tm_yday  # 时间元组，一年中的第几天
print(f'{date[0]}年{date[1]}月{date[2]}日是{date[0]}年第{yday}天')

# 法二
import datetime
date = input()
custom_date = datetime.datetime.strptime(date, %Y/%m/%d).date()
year = custom_date.year
yday = custom_date.timetuple().tm_yday 
print(f'{year}年的第{yday}天')