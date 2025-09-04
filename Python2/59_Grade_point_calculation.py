# 计算绩点

'''
成绩	等级	绩点
90-100	A	4.0
85-89	A-	3.7
82-84	B+	3.3
78-81	B	3.0
75-77	B-	2.7
72-74	C+	2.3
68-71	C	2.0
64-67	C-	1.5
60-63	D	1.3
补考60	D-	1.0
60以下	F	0
平均绩点:(课程学分1*绩点+课程学分2*绩点+课程学分n*绩点)/(课程学分1+课程学分2+课程学分n)
'''
#用户循环输入五分制成绩和课程学分，计算学生平均绩点。
score = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.5, 'D': 1.3, 'D-': 1.0,
         'F': 0.0}
gpaSum, creditSum, gpaAve = 0, 0, 0
while True:
    s = input()
    if s == '-1':
        break
    elif s in score.keys():
        credit = float(input()) # 太妙了！
        gpaSum += score[s] * credit
        creditSum += credit
        gpaAve = gpaSum / creditSum
    else:
        print('data error')
print('{:.2f}'.format(gpaAve))
