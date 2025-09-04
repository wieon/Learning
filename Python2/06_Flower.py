"""
# 4 petals
import turtle as t
for i in range(4):
    t.right(90)
    t.circle(50,180) # 半径，角度
"""
	
# 12 petals
import turtle as t
t.fillcolor("yellow")
t.begin_fill()
for i in range(12):
    t.circle(120,90) # 90°真的妙！
    t.left(120)
t.end_fill()
t.hideturtle()
t.done()

"""
# 12 petals Edition II
import turtle as t
t.colormode(255)

t.color(218,68,214)
t.fillcolor(218,112,214) # dark pink
t.begin_fill()
for i in range(12):
    t.circle(120,60)
    t.left(120)
    t.circle(120,60)
    t.left(90)
t.end_fill()

t.color(238,118,238)
t.fillcolor(238,148,230) # dark pink
t.begin_fill()
for i in range(12):
    t.circle(100,60)
    t.left(120)
    t.circle(100,60)
    t.left(90)
t.end_fill()

t.color(238,178,244)
t.fillcolor(238,218,244) # light pink
t.begin_fill()
for i in range(12):
    t.circle(50,60)
    t.left(120)
    t.circle(50,60)
    t.left(90)
t.end_fill()

t.hideturtle()
t.done()
"""