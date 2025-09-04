import turtle as t

t.pensize(5 )
t.pencolor("yellow")
t.fillcolor("red")

t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)
t.end_fill()

t.hideturtle()   #隐藏画笔
t.done()         #结束绘制

