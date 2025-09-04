import turtle
n = 10
for i in range(1,10,1):
    for j in [90,180,-90,0]:
        turtle.seth (j)
        turtle.fd(n)
        n += 5
		
# 法二
import turtle as t
for i in range(1,37):
	t.seth(90*i)
	t.fd(5*i)