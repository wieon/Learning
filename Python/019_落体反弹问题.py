# 一个球从100米高度自由落下，每次落地后反弹回原高度的一半，
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

height = 100
count = 1
distance = 0
while count <= 10:
	distance += height
	height /= 2
	distance += height
	count += 1

print(f'第10次落地时共经过{distance-height}米，第10次反弹{height}米')