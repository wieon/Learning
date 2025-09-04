'''
import numpy as np
d = input()
date1 = np.array([eval(d[0:4]),eval(d[5:7]),eval(d[8:10])])
date2 = np.array([eval(d[21:25]),eval(d[26:28]),eval(d[29:31])])
date3 = date2 - date1
n = np.array([365,30,1])
print(np.dot(date3, n))
#失败，如果遇到开头是01、03之类的数字就无法表示了
'''

from datetime import datetime
d = input()
date_string1 = '%s-%s-%s' %(d[0:4],d[5:7],d[8:10])
date_string2 = '%s-%s-%s' %(d[21:25],d[26:28],d[29:31])
date1 = datetime.strptime(date_string1, "%Y-%m-%d")
date2 = datetime.strptime(date_string2, "%Y-%m-%d")
delta = date2 - date1
print(delta.days)
