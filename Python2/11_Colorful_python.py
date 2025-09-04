import turtle as t
t.right(30)
t.penup()
t.goto(-200,0)
t.pendown()
t.pensize(30)
for i in ["red","blue","green","yellow"]:  # 蛇身
	t.pencolor(i)
	t.circle(50,60)
	t.circle(-50,60)
t.left(30)
t.pencolor("purple")  # 蛇头
t.fd(50)
t.circle(20,180)
t.fd(40)
t.dot(7,"black")  # 眼睛
t.hideturtle()
t.done()