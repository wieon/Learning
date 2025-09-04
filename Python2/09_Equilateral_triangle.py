# 法一
import turtle as t
import math
length_of_side = eval(input())
height = length_of_side / 2 * math.sqrt(3)

def trangle():  # 画一个三角形
	for i in range(3):
		t.fd(length_of_side)
		t.left(120)
		
trangle()  # 第一个三角形
t.penup()
t.fd(length_of_side/2)
t.left(90)
t.fd(height)
t.right(90)
t.pendown()
trangle()  # 第二个三角形
t.penup()
t.fd(length_of_side/2)
t.right(90)
t.fd(height)
t.left(90)
t.pendown()
trangle()  # 第三个三角形
t.done()

# 法二
import turtle as t
import math
length_of_side = eval(input())
x = length_of_side / 2
y = length_of_side / 2 * math.sqrt(3)
t.goto(2*x,2*y)
t.goto(4*x,0)
t.goto(2*x,0)
t.goto(x,y)
t.goto(3*x,y)
t.goto(2*x,0)
t.goto(0,0)
t.done()